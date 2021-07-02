from django.db import models
from .people import People


class Order(models.Model):
    client = models.ForeignKey(People, on_delete=models.PROTECT, related_name='orders', verbose_name='client')

    def __str__(self):
        return f'Order :{self.pk} - Client: {self.client.name}'


class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=255)
    order = models.ManyToManyField(Order)

    def __str__(self):
        return self.name