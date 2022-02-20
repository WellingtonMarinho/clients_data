from random import randint
from order.models import Order, Product, OrderItems
from clients.models import People


class OrderGenerator():

    def random_id(self, model):
        return randint(1, model.objects.count())

    def get_object(self, instance):
        instance_id = self.random_id(instance)
        return instance.objects.get(id=instance_id)


    def create_order(self):
        order = Order.objects.create(client=self.get_object(People))

        list_products = [self.get_object(Product) for _ in range(randint(1, 4))]

        for each_product in list_products:
            order_items = OrderItems.objects.create(order=order, product=each_product, quantity=randint(1, 5))

        return order_items
