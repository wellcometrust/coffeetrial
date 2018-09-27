import random
from flask import Blueprint, jsonify, render_template, request
from app import db
from models import User, Match, Round


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


@matching_blueprint.route('/match/<int:user>', methods=['GET'])
def get_random_profiles(user):
    random.seed()
    matches = Match.query.filter_by(
        user_1=user
    ).all()
    matches = [match.user_2 for match in matches]
    matches.append(user)
    users = User.query.filter(
        User.id.notin_(matches)
    ).filter_by(locked=False).filter_by(active=True)
    users = [user.to_dict() for user in users.all()]
    if len(users) > 2:
        users = random.sample(users, 3)
    return jsonify(users), 200


@matching_blueprint.route('/match', methods=['POST'])
def set_match():
    response_item = {
        'status': 'failed',
        'message': '',
    }
    post_data = request.get_json()
    user_1 = User.query.get_or_404(post_data.get('user_1_id'))
    user_2 = User.query.get_or_404(post_data.get('user_2_id'))

    if user_1.locked or user_2.locked:
        response_item['message'] = 'Couldn\'t match users (user locked).'
        return jsonify(response_item), 400

    if not (user_1.active and user_2.active):
        response_item['message'] = 'Couldn\'t match users (user inactive).'
        return jsonify(response_item), 400

    current_round = Round.query.order_by(Round.date.desc()).first()

    match = Match(user_1.id, user_2.id, current_round.id)
    db.session.add(match)

    user_1.locked = True
    user_2.locked = True

    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()
    response_item['message'] = 'Users successfully matched!'
    response_item['status'] = 'success'
    return jsonify(response_item), 201
