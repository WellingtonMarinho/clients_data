from django.test import TestCase
from order.models import People, Order, OrderItems, Product
from clients.utils.people_generator import ToPopulateDatabase


class OrderModelTestCase(TestCase):

    def setUp(self):
        to_people = ToPopulateDatabase()
        data_people = to_people.build_people()
        self.people = People.objects.create(**data_people)
        self.product = Product.objects.create(name='Xbox', price=5550.36)
        self.order = Order.objects.create(client=self.people)
        self.order_item = OrderItems.objects.create(product=self.product, order=self.order, quantity=666)

    def test_str_order(self):
        self.assertEqual(str(self.order), str(self.people))

    def test_str_order_items(self):
        dunder_str = f'{self.product.name} - {self.order.client}'
        self.assertEqual(str(self.order_item), dunder_str)

    def test_total_per_item_in_order_items(self):
        result = self.order_item.total_per_item
        expected = self.order_item.product.price * self.order_item.quantity
        self.assertEqual(result, expected)

    def test_total_order(self):
        result = self.order.total_order
        expected = sum([item.total_per_item for item in self.order.items.all()])
        self.assertEqual(result, expected)
