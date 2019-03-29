from flask import Blueprint, render_template, redirect, url_for
from models import Match, Round, User
from client.authentication import is_logged, get_logged_user
from app import db


user_blueprint = Blueprint(
    'user',
    __name__,
    template_folder='./templates'
)


@user_blueprint.route('/optin', methods=['GET'])
@is_logged
def toggle_optin():
    user = get_logged_user()
    user.active = not user.active
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('user.index_view'))


@user_blueprint.route('/', methods=['GET'])
@is_logged
def index_view():
    user = get_logged_user()
    cur_round = Round.query.order_by(Round.date.desc()).first()
    cur_match = Match.query.filter_by(
        round=cur_round.id,
        user_1=user.id
    ).first()

    m_user = None
    if cur_match:
        m_user = User.query.filter_by(id=cur_match.user_2).first()

    return render_template('user/index.html', user=user, m_user=m_user)
