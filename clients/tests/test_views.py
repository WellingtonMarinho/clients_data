from django.test import TestCase


class ViewsPeopleTest(TestCase):
    # def setUp(self):
    #     self.client = self.client

    def test_get(self):
        self.assertEqual(200, self.client.get('/elastic/').status_code)

    def test_return_itens_per_page(self):
        per_page = 15
        response = self.client.get(f'/elastic/?per_page={per_page}').json().get('results')
        self.assertEqual(per_page, len(response))

    def test_max_itens_per_query(self):
        limit_per_query = 69
        response = self.client.get(f'/elastic/?limit_per_query={limit_per_query}').json().get('count')
        self.assertEqual(limit_per_query, response)

    def test_filter_by_sex(self):
        per_page = 5 # limit number to run fast test
        sexs = ['Masculino', 'Feminino']

        for sex in sexs:
            with self.subTest():
                responses = self.client.get(
                    f'/elastic/?sex={sex}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(sex, response.get('sex'))

    def test_filter_by_favorite_color(self):
        per_page = 5
        favorite_colors = ['azul', 'amarelo', 'preto', 'vermelho', 'verde', 'roxo', 'laranja']

        for color in favorite_colors:
            with self.subTest():
                responses = self.client.get(
                    f'/elastic/?favorite_color={color}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(color, response.get('favorite_color'))

    def test_filter_by_weight_range(self):
        per_page = 5
        labels = ['obesity', 'under_weight', 'right_weight', 'overweight' ]

        for label in labels:
            with self.subTest():
                responses = self.client.get(
                    f'/elastic/?weight_range={label}&per_page={per_page}'
                ).json()['results']
                for response in responses:
                    self.assertEqual(label, response.get('weight_range'))
