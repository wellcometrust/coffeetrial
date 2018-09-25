from flask import Blueprint, jsonify


matching_blueprint = Blueprint(
    'matching',
    __name__,
    template_folder='./templates'
)


@matching_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
