import json
import unittest
from tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_user_ping(self):
        """Ensure the /ping route behaves correctly."""
        with self.client:
            response = self.client.get('/admin/user/ping')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('pong', data['message'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
