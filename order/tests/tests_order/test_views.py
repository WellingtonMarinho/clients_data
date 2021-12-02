import json
from django.test import TestCase
from clients.tests.factories import PeopleGenerator
from order.tests.factories import ProductsGenerator


class OrderPostAPIViewTestCase(TestCase):
    def setUp(self):
        people_generator = PeopleGenerator()
        products_generator = ProductsGenerator()

        self.products = products_generator.save_data()
        self.people = people_generator.save_people()
        self.endpoint = f'/api/orders/'
        self.headers = 'application/json'

        self.body = {
            "client": 1,
            "items": [
                {
                    "product": 2,
                    "quantity": 12
                },
                {
                    "product": 5,
                    "quantity": 2
                },
                {
                    "product": 12,
                    "quantity": 6
                },
                {
                    "product": 1,
                    "quantity": 2
                }
             ]
        }

    # def test_get_order_status_code(self):
    #
    #     response = self.client.get(self.endpoint)
    #     self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        # print(self.endpoint)
        # print()
        # print(json.dumps(self.body))
        # print()
        response = self.client.post(self.endpoint, body=json.dumps(self.body), content_type=self.headers)
        print(dir(response))
        print(response.json())
        print()
        print()
        print()
        self.assertEqual(response.status_code, 201)
        # print(self.people)
        # print()
        # print(response.json())
        # print()
        # print()
        # print()
        # print(dir(response))

