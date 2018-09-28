import random
from flask import Blueprint, jsonify, render_template, request
from app import db
from models import User, Match, Round


matching_blueprint = Blueprint(
    'matching',
    __name__,
    template_folder='./templates'
)


def get_random_user_set(user):
    random.seed()
    matches = Match.query.filter_by(
        user_1=user.id
    ).all()
    matches = [match.user_2 for match in matches]
    matches.append(user.id)
    users = User.query.filter(
        User.id.notin_(matches)
    ).filter_by(locked=False).filter_by(active=True)
    return [user.to_dict() for user in users.all()]


def match_users(user_1, user_2):
    if user_1.locked or user_2.locked:
        return {'status': False, 'msg': 'user locked'}

    if not (user_1.active and user_2.active):
        return {'status': False, 'msg': 'user inactive'}

    current_round = Round.query.order_by(Round.date.desc()).first()

    match = Match(user_1.id, user_2.id, current_round.id)
    db.session.add(match)

    user_1.locked = True
    user_2.locked = True

    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()
    return {'status': True, 'object': match.to_dict()}


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
    user = User.query.get_or_404(user)
    users = get_random_user_set(user)
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

    match = match_users(user_1, user_2)
    if not match['status']:
        response_item['message'] = f"Couldn't match users ({match['msg']})."
        return jsonify(response_item), 400

    response_item['match'] = match['object']
    response_item['message'] = 'Users successfully matched!'
    response_item['status'] = 'success'
    return jsonify(response_item), 201


@matching_blueprint.route('/match/random', methods=['POST'])
def set_match_random():
    response_item = {
        'status': 'failed',
        'message': '',
    }
    post_data = request.get_json()
    user = User.query.get_or_404(post_data.get('user_id'))

    users = get_random_user_set(user)
    if not users:
        response_item['message'] = 'No free user to match with.'
        return jsonify(response_item), 400

    user_2 = random.choice(users)
    user_2 = User.query.get_or_404(user_2['id'])

    match = match_users(user, user_2)
    if not match['status']:
        response_item['message'] = f"Couldn't match users ({match['msg']})."
        return jsonify(response_item), 400

    response_item['match'] = match['object']
    response_item['message'] = 'Users successfully matched!'
    response_item['status'] = 'success'
    return jsonify(response_item), 201
