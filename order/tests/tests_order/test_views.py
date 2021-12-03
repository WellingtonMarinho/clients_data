from django.test import TestCase
from clients.tests.factories import PeopleGenerator
from order.tests.factories import ProductsGenerator
from order.models import Order

class OrderPostAPIViewTestCase(TestCase):
    def setUp(self):
        people_generator = PeopleGenerator()
        products_generator = ProductsGenerator()

        self.products = [products_generator.save_data() for _ in range(10)]
        self.list_people = [people_generator.save_people() for _ in range(10)]
        self.endpoint = f'/api/orders/'
        self.headers = 'application/json'
        print(self.products)
        print(self.list_people)
        self.body = {"client": 1,"items": [{"product": 2, "quantity": 12}]}

    # def test_get_order_status_code(self):
    #
    #     response = self.client.get(self.endpoint)
    #     self.assertEqual(response.status_code, 200)

    def test_create_order_status_code(self):
        response = self.client.post(
            self.endpoint,
            self.body,
            self.headers
        )
        print()
        print(response.json())
        print()
        print()
        print()
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
