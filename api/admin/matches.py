import tempfile
import os

from datetime import datetime
from flask import (Blueprint, jsonify, request, flash, redirect,
                   url_for, render_template)
from models import Match, Round
from match_users import unlock_all_users, match_all_users, import_from_csv
from app import db
from client.authentication import is_admin


matches_blueprint = Blueprint(
    'matches',
    __name__,
    template_folder='./templates'
)


@matches_blueprint.route('/admin/ping', methods=['GET'])
@is_admin
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )


@matches_blueprint.route('/admin/matches', methods=['GET'])
@is_admin
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
@is_admin
def list_matches_by_round(round_id):
    round = Round.query.get_or_404(round_id)
    matches = Match.query.filter_by(round=round.id).all()
    matches = [match.to_dict() for match in matches]

    return jsonify({
        'status': 'success',
        'round_id': round.id,
        'matches': matches
    })


@matches_blueprint.route('/admin/matches/import', methods=['GET', 'POST'])
@is_admin
def import_csv():
    if request.method != "POST":
        return render_template('admin/upload.html')
    # Check if the post request has the file part
    if 'data_file' not in request.files or 'matches_file' not in request.files:
        flash('You didn\'t include a file. (No file attribute)')
        return redirect(url_for('matches.import_csv'))
    data_file = request.files['data_file']
    matches_file = request.files['matches_file']
    if data_file.filename == '':
        flash('You didn\'t include a file. (No filenames)')
        return redirect(url_for('matches.import_csv'))
    data_filename = data_file.filename
    matches_filename = matches_file.filename
    with tempfile.TemporaryDirectory() as tf:

        data_file.save(os.path.join(tf, data_filename))
        matches_file.save(os.path.join(tf, matches_filename))

        import_from_csv(
            os.path.join(tf, data_filename),
            os.path.join(tf, matches_filename)
        )

    return redirect(url_for('matches.list_matches_cur_round'))


@matches_blueprint.route('/admin/matches/new', methods=['GET'])
@is_admin
def create_new_matches():

    # TODO: Do a 2 step confirmation

    round = Round(datetime.now())
    db.session.add(round)
    db.session.commit()

    unlock_all_users()
    unmatched = match_all_users()

    return jsonify({
        'status': 'success',
        'round_id': round.id,
        'unmatched users': unmatched,
    })
