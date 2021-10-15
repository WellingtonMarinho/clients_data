from django.test import TestCase
from clients.models import People


class ViewsPeopleTest(TestCase):
    def setUp(self):
        self.people_to_request = People.objects.create(
            name='Letícia Esther Viana',
            cpf='953.183.769-40',
            rg='24.286.324-3',
            birth_date='1961-11-13',
            sex='Feminino',
            sign='Escorpião',
            mother_name='Ana Elisa',
            father_name='Lucca Sebastião Viana',
            email='leticiaestherviana_@focusgrafica.com.br',
            telefone_number='() 2576-9555',
            mobile='() 99486-7953',
            height=1.64,
            weight=45,
            type_blood='A+',
            favorite_color='laranja'
        )

    def test_get(self):
        self.assertEqual(200, self.client.get('/people/').status_code)

    def test_get_detail_object(self):
        people = People.objects.last()
        slug = people.slug

        response = self.client.get(f'/people/{slug}/').json()

        self.assertEqual(people.name, response['name'])
        self.assertEqual(people.rg, response['rg'])
        self.assertEqual(people.cpf, response['cpf'])

    def test_return_itens_per_page(self):
        per_page = 15
        response = self.client.get(f'/people/?per_page={per_page}').json().get('results')
        self.assertEqual(per_page, len(response))

    def test_max_itens_per_query(self):
        limit_per_query = 69
        response = self.client.get(f'/people/?limit_per_query={limit_per_query}').json().get('count')
        self.assertEqual(limit_per_query, response)

    def test_filter_by_sex(self):
        per_page = 5 # limit number to run fast test
        sexs = ['Masculino', 'Feminino']

        for sex in sexs:
            with self.subTest():
                responses = self.client.get(
                    f'/people/?sex={sex}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(sex, response.get('sex'))

    def test_filter_by_favorite_color(self):
        per_page = 5
        favorite_colors = ['azul', 'amarelo', 'preto', 'vermelho', 'verde', 'roxo', 'laranja']

        for color in favorite_colors:
            with self.subTest():
                responses = self.client.get(
                    f'/people/?favorite_color={color}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(color, response.get('favorite_color'))

    def test_filter_by_weight_range(self):
        per_page = 5
        labels = ['obesity', 'under_weight', 'right_weight', 'overweight' ]

        for label in labels:
            with self.subTest():
                responses = self.client.get(
                    f'/people/?weight_range={label}&per_page={per_page}'
                ).json()['results']
                for response in responses:
                    self.assertEqual(label, response.get('weight_range'))
