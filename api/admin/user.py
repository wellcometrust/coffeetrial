import hashlib

from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, render_template, session
from app import db
from models import User


user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='./templates'
)


def _get_hashed_password(*args):
    password = ''.join(args)
    return hashlib.sha256(password.encode()).hexdigest()


@user_blueprint.route('/admin/users/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )


@user_blueprint.route('/admin/users/logged', methods=['GET'])
def is_logged():
    auth_token = session.get('auth_token')
    user = session.get('auth_user')
    if auth_token and user:
        db_user = User.query.filter_by(email=user).first()
        if db_user.expiracy_time > datetime.now():
            return jsonify(
                {
                    'status': 'success',
                    'message': f'User {db_user.email} is logged',
                    'expiracy_time': db_user.expiracy_time
                }
            )
    return jsonify({
        'status': 'error',
        'message': 'User is not logged',
    })


@user_blueprint.route('/admin/users', methods=['POST'])
def user_create():
    post_data = request.get_json()
    user = User(
        post_data['firstname'],
        post_data['lastname'],
        post_data['email'],
        post_data['active'],
        post_data['department_id'],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': f'{user.email} was added!',
    }), 201


@user_blueprint.route('/admin/login', methods=['GET', 'POST'])
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
        return render_template('admin/login.html')


@user_blueprint.route('/admin/logout', methods=['GET'])
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
