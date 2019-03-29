from flask import Blueprint, jsonify, request
from app import db
from models import User
from client.authentication import is_admin


user_management_blueprint = Blueprint(
    'user_management',
    __name__,
    template_folder='./templates'
)


@user_management_blueprint.route('/admin/users/ping', methods=['GET'])
@is_admin
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )


@user_management_blueprint.route('/admin/users', methods=['POST'])
@is_admin
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
