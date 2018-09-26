import random
from flask import Blueprint, jsonify, render_template
from models import User, Match


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


@matching_blueprint.route('/match/<int:user>/profiles', methods=['GET'])
def get_random_profiles(user):
    random.seed()
    matches = Match.query.filter_by(
        user_1=user
    ).all()
    matches = [match.user_2 for match in matches]
    matches.append(user)
    users = User.query.filter(User.id.notin_(matches)).all()
    users = [user.to_dict() for user in users]
    if len(users) > 2:
        users = random.sample(users, 3)
    return jsonify(users)
