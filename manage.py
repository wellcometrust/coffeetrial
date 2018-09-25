# import unittest
# import coverage
import csv
from datetime import datetime
from flask.cli import FlaskGroup
from models import User, Department, Round, Match

from app import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def import_from_csv():
    departments = set([])
    users = []
    matches = []
    round = Round(datetime.now())
    db.session.add(round)
    with open('datasets/dataset.csv') as csvfile:
        users_csv = csv.DictReader(csvfile, dialect='excel', delimiter=',')
        for i, row in enumerate(users_csv):
            departments.add(row['Department'])
            department = Department.query.filter_by(name=row['Department']).first()
            if not department:
                department = Department(row['Department'])
                db.session.add(department)

            user = User.query.filter_by(email=row['Email address']).first()
            if not user:
                user = User(
                    row['\ufeffFirst name'][0] if row['\ufeffFirst name'] else '',
                    f"Doe{i}{row['Surname'][3:]}",
                    row['Email address'],
                    True if row['Active'] == 'Yes' else False,
                    datetime.now(),
                    department.id
                )
                db.session.add(user)
            users.append(row)
    db.session.commit()

    with open('datasets/matches.csv') as csvfile:
        matches_csv = csv.DictReader(csvfile, dialect='excel', delimiter=',')
        for i, row in enumerate(matches_csv):
            user = User.query.filter_by(email=row['Email']).first()
            if not user:
                continue
            for i in range(1, 27):
                if row.get(f'R{i}'):
                    user2 = User.query.filter_by(
                        email=row.get(f'R{i}')
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

# @cli.command()
# def seed_db():
#     db.session.add(
#         User(username='noelflantier', email='n.flantier@example.com')
#     )
#     db.session.add(
#         User(username='hubertbdelabatte', email='h.bdlbatte@example.com')
#     )
#     db.session.commit()


# @cli.command()
# def test():
#     """Runs the tests without code coverage."""
#     tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1


if __name__ == '__main__':
    cli()
