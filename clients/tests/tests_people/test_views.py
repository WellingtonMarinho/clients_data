from django.urls import reverse
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

        # self.endpoint_detail = reverse('clients:people-detail')
        self.endpoint_collection = reverse('clients:people-search')

    def test_get(self):
        self.assertEqual(200, self.client.get(self.endpoint_collection).status_code)

    def test_get_detail_object(self):
        people = People.objects.last()
        uuid = people.uuid
        url = reverse('clients:people-detail', kwargs={'people_sid': uuid})
        response = self.client.get(f'{url}').json()

        self.assertEqual(people.name, response['name'])
        self.assertEqual(people.rg, response['rg'])
        self.assertEqual(people.cpf, response['cpf'])

    def test_absolute_url_api_detail_with_client(self):
        response = self.client.get(self.people_to_request.absolute_url_api())
        self.assertEqual(200, response.status_code)

    def test_return_itens_per_page(self):
        per_page = 15
        response = self.client.get(f'{self.endpoint_collection}?per_page={per_page}').json().get('results')
        self.assertEqual(per_page, len(response))

    def test_max_itens_per_query(self):
        limit_per_query = 69
        response = self.client.get(f'{self.endpoint_collection}?limit_per_query={limit_per_query}').json().get('count')
        self.assertEqual(limit_per_query, response)

    def test_filter_by_sex(self):
        per_page = 5 # limit number to run fast test
        sexs = ['Masculino', 'Feminino']

        for sex in sexs:
            with self.subTest():
                responses = self.client.get(
                    f'{self.endpoint_collection}?sex={sex}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(sex, response.get('sex'))

    def test_filter_by_favorite_color(self):
        per_page = 5
        favorite_colors = ['azul', 'amarelo', 'preto', 'vermelho', 'verde', 'roxo', 'laranja']

        for color in favorite_colors:
            with self.subTest():
                responses = self.client.get(
                    f'{self.endpoint_collection}?favorite_color={color}&per_page={per_page}'
                ).json().get('results')
                for response in responses:
                    self.assertEqual(color, response.get('favorite_color'))

    def test_filter_by_weight_range(self):
        per_page = 5
        labels = ['obesity', 'under_weight', 'right_weight', 'overweight' ]

        for label in labels:
            with self.subTest():
                responses = self.client.get(
                    f'{self.endpoint_collection}?weight_range={label}&per_page={per_page}'
                ).json()['results']
                for response in responses:
                    self.assertEqual(label, response.get('weight_range'))
