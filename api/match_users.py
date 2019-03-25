from models import Match, Round, User
from app import db


def get_random_user_set(user):
    """Get a list of yet unmatched users for a given user.

    Args:
      * user: The user object to find matches for.
    """

    matches = Match.query.filter_by(
        user_1=user.id
    ).all()
    matches = [match.user_2 for match in matches]
    matches.append(user.id)
    users = User.query.filter(
        User.id.notin_(matches)
    ).filter(
        User.department_id.notin_([user.department_id])
    ).filter_by(locked=False).filter_by(active=True)
    return users.all()


def match_users(user_1, user_2):
    """Matches two users and lock them.

    Args:
      * user_1: The user object of the user.
      * user_2: The user object of the user to match user_1 with.

    Returns:
      * status: A dict containing a status (True|False) and either the match
    object or an error message.
    """

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


def unlock_all_users():
    """Set all user status to "unlocked" to match them this round."""

    users = User.query.all()
    for user in users:
        user.locked = False
        db.session.add(user)

    db.session.commit()


def match_all_users():
    """Match all users into a pair of never matched.

    Uses a very basic algorithme of "Match the ones with less possibility
    first". This should be replaced by a graph exploration.
    """

    users = User.query.filter_by(active=True).all()
    matching = []
    for user in users:
        m_users = get_random_user_set(user)
        matching.append({
            'user': user,
            'matches': len(m_users)
        })

    # Match the users with the less matching possibility first
    matching = sorted(matching, key=lambda matchs: matchs['matches'])

    for match in matching:
        # Stop if we already matched this user
        if match['user'].locked:
            continue

        # Find all compatible unmatched users
        m_user = get_random_user_set(match['user'])
        if not m_user:
            continue

        match_users(match['user'], m_user[0])

    unmatched_users = User.query.filter_by(
        locked=False
    ).filter_by(
        active=True
    ).all()

    return [u.to_dict() for u in unmatched_users]
