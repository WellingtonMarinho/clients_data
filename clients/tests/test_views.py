from django.test import TestCase


class ViewsPeopleTest(TestCase):
    def setUp(self):
        self.client = self.client

    def test_get(self):
        self.assertEqual(200, self.client.get('/elastic/').status_code)

