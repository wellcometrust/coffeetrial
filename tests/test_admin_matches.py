import json
import unittest
from datetime import datetime
from tests.base import BaseTestCase
from models import User, Match, Department, Round
from app import db


def _add_department():
    department = Department('test')
    db.session.add(department)


def _add_user(fname, lname, email):
    db.session.commit()
    user = User(
        fname,
        lname,
        email,
        True,
        1
    )
    db.session.add(user)
    db.session.commit()
    return user


def _add_round():
    round = Round(datetime.now())
    db.session.add(round)
    db.session.commit()


def _add_match(user_1, user_2):
    match = Match(user_1.id, user_2.id, 1)
    db.session.add(match)
    db.session.commit()
    return match


class TestMatchesService(BaseTestCase):
    """Tests for the Users Service."""

    def test_matches_ping(self):
        """Ensure the /ping route behaves correctly."""
        with self.client:
            response = self.client.get('/admin/ping')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pong', data['message'])
            self.assertIn('success', data['status'])

    def test_matches_list(self):
        """Ensure that the admin matches list view behave correctly."""
        _add_department()
        _add_round()
        user = _add_user('john', 'doe', 'j.doe@example.com')
        user_2 = _add_user('dany', 'doe', 'd.doe@example.com')
        _add_user('george', 'doe', 'g.doe@example.com')
        _add_user('vince', 'doe', 'v.doe@example.com')
        _add_match(user, user_2)
        with self.client:
            response = self.client.get('/admin/matches')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())
            self.assertTrue(len(data['matches']) > 0)
            self.assertIn('success', data['status'])
            self.assertIn('id', data['matches'][0].keys())


if __name__ == '__main__':
    unittest.main()
