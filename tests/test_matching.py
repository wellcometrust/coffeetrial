import json
import unittest
from tests.base import BaseTestCase
from app import db
from datetime import datetime
from models import User, Department, Match, Round


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


class TestMatchingService(BaseTestCase):
    """Tests for the Users Service."""

    def test_matching_ping(self):
        """Ensure the /ping route behaves correctly."""
        with self.client:
            response = self.client.get('/ping')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pong', data['message'])
            self.assertIn('success', data['status'])

    def test_main_no_users(self):
        """Ensure the main route behave correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_match_rand_profiles(self):
        """Ensure the match route send random unlinked profiles"""
        _add_department()
        _add_round()
        user = _add_user('john', 'doe', 'j.doe@example.com')
        user_2 = _add_user('dany', 'doe', 'd.doe@example.com')
        _add_user('george', 'doe', 'g.doe@example.com')
        _add_user('vince', 'doe', 'v.doe@example.com')
        _add_match(user, user_2)
        response = self.client.get(f'/match/{user.id}/profiles')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)
        ids = [user['id'] for user in response.json]
        self.assertNotIn(user.id, ids)
        self.assertNotIn(user_2.id, ids)


if __name__ == '__main__':
    unittest.main()
