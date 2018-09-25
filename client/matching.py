from flask import Blueprint, jsonify, render_template


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


@matching_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
