from flask import Blueprint, jsonify
from models import Match, Round


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


@matches_blueprint.route('/admin/matches', methods=['GET'])
def list_matches_cur_round():
    cur_round = Round.query.order_by(Round.date.desc()).first()
    matches = Match.query.filter_by(round=cur_round.id).all()
    matches = [match.to_dict() for match in matches]

    return jsonify({
        'status': 'success',
        'round_id': cur_round.id,
        'matches': matches
    })


@matches_blueprint.route('/admin/matches/<int:round_id>', methods=['GET'])
def list_matches_by_round(round_id):
    round = Round.query.get_or_404(round_id)
    matches = Match.query.filter_by(round=round.id).all()
    matches = [match.to_dict() for match in matches]

    return jsonify({
        'status': 'success',
        'round_id': round.id,
        'matches': matches
    })
