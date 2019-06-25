import unittest
import getpass
import click
from sqlalchemy.exc import ProgrammingError
from datetime import datetime
from flask.cli import FlaskGroup
from models import User, Round
from match_users import unlock_all_users, match_all_users, import_from_csv
from client.authentication import _get_hashed_password

from app import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
@click.option('--force', flag_value=False)
def recreate_db(force):
    try:
        r = Round.query.all()
        if r and force:
            print('force=True ; Dropping existing database')
            db.drop_all()
    except ProgrammingError:
        print('database doesn\'t exists. Not dropping.')
    finally:
        db.create_all()
        db.session.commit()


@cli.command()
def import_csv():
    import_from_csv('datasets/dataset.csv', 'datasets/matches.csv')


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def new_round():
    """Runs a new match round:
      * Unlock all users
      * Create a new round
      * Match all users together
    """
    round = Round(datetime.now())
    db.session.add(round)
    db.session.commit()

    unlock_all_users()
    unmatched = match_all_users(enable_mailing=False)

    return unmatched


@cli.command()
@click.argument('firstname')
@click.argument('lastname')
@click.argument('email')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def add_superuser(firstname, lastname, email, password=None):
    if not password:
        password = getpass()
    s_user = User(
        firstname=firstname,
        lastname=lastname,
        email=email,
        active=True,
    )
    s_user.password = _get_hashed_password(password)
    s_user.is_admin = True
    db.session.add(s_user)
    db.session.commit()


if __name__ == '__main__':
    cli()
