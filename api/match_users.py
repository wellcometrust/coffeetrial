import csv

from datetime import datetime

from models import Match, Round, User, Department
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
        User.id.notin_(matches),
        User.department_id.notin_([user.department_id])
    ).filter_by(locked=False, active=True, is_admin=False)
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

    users = User.query.filter_by(
        active=True,
        is_admin=False
    ).all()
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


def import_from_csv(csv_path, matches_csv_path):
    departments = set([])
    users = []
    matches = []
    with open(csv_path) as csvfile:
        users_csv = csv.DictReader(csvfile, dialect='excel', delimiter=',')
        for i, row in enumerate(users_csv):
            departments.add(row['Department'])
            department = Department.query.filter_by(
              name=row['Department']
            ).first()
            if not department:
                department = Department(row['Department'])
                db.session.add(department)

            user = User.query.filter_by(email=row['Email address']).first()
            if not user:
                email = ''.join([
                    row['Email address'][:1],
                    'doe',
                    row['Email address'][4:]
                ])
                user = User(
                  firstname=row['First name'][0] if row['First name'] else '',
                  lastname=f"Doe{i}{row['Surname'][3:]}",
                  email=email,
                  active=True if row['Active'] == 'Yes' else False,
                  department_id=department.id
                )
                db.session.add(user)
            users.append(row)
    db.session.commit()

    with open(matches_csv_path) as csvfile:
        matches_csv = csv.DictReader(csvfile, dialect='excel', delimiter=',')
        for i, row in enumerate(matches_csv):
            base_email = ''.join([
                row['Email'][:1],
                'doe',
                row['Email'][4:]
            ])
            user = User.query.filter_by(email=base_email).first()
            if not user:
                continue
            for i in range(1, 27):
                if row.get(f'R{i}'):
                    round = Round.query.filter_by(id=i).first()
                    if not round:
                        round = Round(datetime.now())
                        db.session.add(round)
                        db.session.commit()
                    email = row.get(f'R{i}')
                    email = ''.join([
                        email[:1],
                        'doe',
                        email[4:]
                    ])
                    user2 = User.query.filter_by(
                        email=email
                    ).first()
                    if user2:
                        match = Match(user.id, user2.id, round.id)
                        db.session.add(match)
                        matches.append(match)
    print(
        f'[+] Imported {len(matches)} matches and {len(users)}',
        f'users from {len(departments)} departments.'
    )
    db.session.commit()
