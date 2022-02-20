from django.test import TestCase
from clients.tests.factories import PeopleGenerator
from order.tests.factories import ProductsGenerator
from order.models import Order, Product
from clients.models import People


class OrderPostAPIViewTestCase(TestCase):
    def setUp(self):
        self.people_generator = PeopleGenerator()
        self.products_generator = ProductsGenerator()
        self.products = self.products_generator.save_data()
        self.list_people = [self.people_generator.save_people() for _ in range(3)]

        self.endpoint = f'/api/orders/'
        self.headers = 'application/json'

        self.body = {"client": People.objects.last().id,"items": [{"product": Product.objects.last().id, "quantity": 12}]}

    def test_get_order_status_code(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, 200)

    def test_create_order_status_code(self):
        self.products_generator.save_data()
        self.people_generator.save_people()
        response = self.client.post(
            path=self.endpoint,
            data=self.body,
            content_type=self.headers
        )
        self.assertEqual(response.status_code, 201)

    def test_count_in_database_after_create_order(self):
        quantity = 5
        count_before = Order.objects.count()
        for _ in range(quantity):
            with self.subTest():
                response = self.client.post(
                    self.endpoint,
                    self.body,
                    self.headers
                )
        self.assertEqual((count_before + quantity), Order.objects.count())
