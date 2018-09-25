from flask import Blueprint, jsonify


user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='./templates'
)


@user_blueprint.route('/admin/user/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
