from flask import Blueprint, jsonify


round_blueprint = Blueprint(
    'round',
    __name__,
    template_folder='./templates'
)


@round_blueprint.route('/admin/round/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
