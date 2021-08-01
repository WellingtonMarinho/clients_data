from django.db import models
from django.db.models import Avg, Sum
from django.utils.translation import gettext_lazy as _
from . import BaseModel, People


class Order(BaseModel):
    client = models.ForeignKey(
        People,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('client')
    )

    def __str__(self):
        return f'Order: {self.pk} - Client: {self.client.name} -- Total R$ {self.total}'

# TODO Aplicar com o annotate
    @property
    def total(self):
        return self.order_product.all().aggregate(Sum('product__price'))

    @property
    def teste(self):
        return self.order_product.product.annotate(total=Sum('product__price'))

    @property
    def media_per_item(self):
        return self.order_product.all().aggregate(Avg('product__price'))


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=55)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    description = models.TextField(_('Description'), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_product',
        verbose_name=_('Order')
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order',
        verbose_name=_('Product')
    )
    quantity = models.IntegerField(_('Quantity'), default=1)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return self.product

    @property
    def total_per_product(self):
        return self.product.price * self.quantity
