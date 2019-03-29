from flask import Blueprint, jsonify
from client.authentication import is_admin


round_blueprint = Blueprint(
    'round',
    __name__,
    template_folder='./templates'
)


@round_blueprint.route('/admin/round/ping', methods=['GET'])
@is_admin
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
