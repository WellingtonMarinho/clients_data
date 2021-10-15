from django.db import models
from django.db.models import Avg, Sum
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from . import BaseModel, People


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=55)
    price = models.DecimalField(_('Price'), max_digits=8, decimal_places=2)
    description = models.TextField(_('Description'), max_length=255, blank=True, null=True)
    slug = AutoSlugField(
        populate_from=['name',],
        editable=False,
        unique=True,
        verbose_name='Slug'
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.name

    def absolute_url_api(self):
        return reverse("products-detail", kwargs={'product_slug': self.slug})


class OrderItems(models.Model):
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.product.name


class Order(models.Model):
    client = models.ForeignKey('People', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.client.name