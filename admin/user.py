from flask import Blueprint, jsonify, request
from app import db
from models import User


user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='./templates'
)


@user_blueprint.route('/admin/users/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )


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
