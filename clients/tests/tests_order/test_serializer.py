from django.test import TestCase
from clients.models import People, Order, OrderItems, Product
from clients.utils.people_generator import ToPopulateDatabase
from clients.serializers import OrderSerializer, OrderPOSTSerializer


class OrderSerializerTestCase(TestCase):

    def setUp(self):
        to_people = ToPopulateDatabase()
        data_people = to_people.build_people()
        self.people = People.objects.create(**data_people)
        self.product = Product.objects.create(name='Xbox', price=5550.36)
        self.order = Order.objects.create(client=self.people)
        self.order_item = OrderItems.objects.create(product=self.product, order=self.order, quantity=666)
        self.serializer_get = OrderSerializer(self.order)

    def test_contains_expected_fields_in_serializer_get(self):
        result = self.serializer_get.data.keys()
        expected = ['id', 'client', 'items', 'total_order']
        self.assertEqual(set(result), set(expected))

