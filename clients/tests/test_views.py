from django.test import TestCase



class ViewsPeopleTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)



