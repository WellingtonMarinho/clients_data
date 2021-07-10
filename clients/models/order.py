from django.db import models
from .people import People
# from django_better_admin_arrayfield.models.fields import ArrayField


class Order(models.Model):
    client = models.ForeignKey(People, on_delete=models.PROTECT, related_name='orders', verbose_name='client')

    def __str__(self):
        return self.client.name

    @property
    def name(self):
        return self.client.name


class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return self.pk
