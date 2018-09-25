import json
import unittest
from tests.base import BaseTestCase


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

    def test_main_no_users(self):
        """Ensure the main route behave correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
