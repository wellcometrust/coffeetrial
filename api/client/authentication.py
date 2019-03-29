import hashlib
import logging

from datetime import datetime, timedelta
from functools import wraps

from flask import (Blueprint, jsonify, request, render_template, session,
                   redirect, url_for, flash)
from werkzeug.exceptions import Forbidden, Unauthorized
from app import db
from models import User, Department


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='./templates'
)


def _get_hashed_password(*args):
    password = ''.join(args)
    return hashlib.sha256(password.encode()).hexdigest()


def get_logged_user():
    """Check if the user is logged in or is using auth token.

    Returns:
      * bool: True if a user is authenticated, else False.
    """
    auth_token = None
    # If user is in session, uses session
    if session.get('auth_token') and session.get('auth_user'):
        auth_token = session.get('auth_token')

    # Else, if user uses the json auth, check for request.json
    if request.headers.get('Authorization'):
        auth_token = request.headers.get('Authorization')

    # Finally, try to authenticate with token
    db_user = User.query.filter_by(auth_token=auth_token).first()
    if auth_token and db_user:
        if db_user.expiracy_time > datetime.now():
            return db_user

    return False


def is_logged(func):
    """Decorator checking if the user is logged in.

    Args:
      * func: The function to perform if the user is logged in.

    Returns:
      * wrapper: The wrapped function

    Raises:
      * http.Unauthorized: 401 error if the user isn't logged in.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = get_logged_user()
        if user:
            return func(*args, **kwargs)
        else:
            flash('You need to be logged in to access this page. (401)')
            return redirect(url_for('auth.login'))

    return wrapper


def is_admin(func):
    """Decorator checking if the user is an admin.

    Args:
      * func: The function to perform if the user is logged in.

    Returns:
      * wrapper: The wrapped function

    Raises:
      * http.Unauthorized: 401 error if the user isn't logged in.
      * http.Forbidden: 403 error if the user is logged in but not an admin.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = get_logged_user()
        if user:
            if user.is_admin:
                return func(*args, **kwargs)
            else:
                # User is logged but is not admin
                raise Forbidden()
        else:
            # User is not logged
            raise Unauthorized()

    return wrapper


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        if request.get_json():
            # Request is from api
            post_data = request.get_json()
        else:
            # Request is from form
            post_data = request.form

        if post_data.get('user_email') and post_data.get('user_password'):
            user = User.query.filter_by(
                email=post_data['user_email'],
                password=_get_hashed_password(post_data['user_password']),
                active=True,
            ).first()
            if user and user.password is not None:
                auth_token = _get_hashed_password(
                    user.email,
                    str(datetime.now()),
                    post_data.get('user_password'),
                )
                user.auth_token = auth_token
                user.expiracy_time = datetime.now() + timedelta(days=1)
                session['auth_token'] = auth_token
                session['auth_user'] = user.email

                db.session.add(user)
                db.session.commit()
                return jsonify({
                    'status': 'success',
                    'message': 'Login complete',
                    'auth_token': auth_token,
                    'expiracy_time': user.expiracy_time,
                })
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Unsuccessful login - Wrong id or password'
                })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Unsuccessful login'
            })
    else:
        return render_template('auth/login.html')


@auth_blueprint.route('/logout', methods=['GET'])
def logout():
    if session['auth_user']:
        user = User.query.filter_by(email=session['auth_user']).first()
        user.expiracy_time = datetime.now() - timedelta(days=2)

        db.session.add(user)
        db.session.commit()

    session['auth_user'] = None
    session['auth_token'] = None
    return jsonify({
        'status': 'success',
        'message': 'Successfully logged out.'
    })


@auth_blueprint.route('/signin', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        if request.get_json():
            post_data = request.get_json()
        else:
            post_data = request.form

        fields = [
            'user_email',
            'user_password',
            'user_confirm_password',
            'user_firstname',
            'user_lastname',
            'user_department',
        ]

        missing = False
        for field in fields:
            if field not in post_data:
                flash(f'You need to type in a {field}.')
                missing = True

            if missing:
                return redirect(url_for('auth.create_account'))

        if post_data['user_password'] != post_data['user_confirm_password']:
            flash('Your passwords are not matching.')
            return redirect(url_for('auth.create_account'))

        department = Department.query.filter_by(
            name=post_data['user_department']
        ).first()
        user = User.query.filter_by(email=post_data['user_email']).first()
        if not user:
            user = User(
                firstname=post_data['user_firstname'],
                lastname=post_data['user_lastname'],
                email=post_data['user_email'],
                department_id=department.id,
                active=True,
            )
            user.password = _get_hashed_password(
                post_data['user_password']
            )
        else:
            # If the user has a password, it means the account has already
            # been created. If it hasn't, it only has been imported.
            if user.password:
                return jsonify({
                    'status': 'error',
                    'message': 'A user with this email already exists'
                })
            user.firstname = post_data['user_firstname']
            user.lastname = post_data['user_lastname']
            user.password = post_data['user_password']
            user.active = True

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.index_view'))
    else:
        departments = Department.query.all()
        return render_template('auth/signin.html', departments=departments)
