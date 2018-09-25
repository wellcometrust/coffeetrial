from flask import Blueprint, jsonify


matches_blueprint = Blueprint(
    'matches',
    __name__,
    template_folder='./templates'
)


@matches_blueprint.route('/admin/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
