from django.test import TestCase


class ViewsPeopleTest(TestCase):
    # def setUp(self):
    #     self.client = self.client

    def test_get(self):
        self.assertEqual(200, self.client.get('/elastic/').status_code)

    def test_return_itens_per_page(self):
        value = 15
        response = self.client.get(f'/elastic/?per_page={value}').json()['results']
        self.assertEqual(value, len(response))

    def test_max_itens_per_query(self):
        value = 69
        response = self.client.get(f'/elastic/?limit_per_query={value}').json()['count']
        self.assertEqual(value, response)

    def test_filter_by_sex(self):
        sexs = ['Masculino', 'Feminino']
        for sex in sexs:
            with self.subTest():
                responses = self.client.get(f'/elastic/?sex={sex}').json()['results']
                for response in responses:
                    self.assertEqual(sex, response.get('sex'))
