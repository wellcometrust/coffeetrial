import json
import unittest
from app import db
from tests.base import BaseTestCase
from models import Department


def _add_department():
    department = Department('test')
    db.session.add(department)
    db.session.commit()
    return department


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_user_ping(self):
        """Ensure the /ping route behaves correctly."""
        with self.client:
            response = self.client.get('/admin/users/ping')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pong', data['message'])
            self.assertIn('success', data['status'])

    def test_user_add(self):
        department = _add_department()
        with self.client:
            response = self.client.post(
                '/admin/users',
                data=json.dumps({
                    'firstname': 'john',
                    'lastname': 'doe',
                    'email': 'john.doe@example.com',
                    'active': True,
                    'department_id': department.id,
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode(encoding='utf-8'))
            self.assertEqual(response.status_code, 201)
            self.assertIn('john.doe@example.com was added!', data['message'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
