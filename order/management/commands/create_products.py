from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from order.tests.factories import ProductsGenerator
from order.models import Product


class Command(BaseCommand):
    help = _('Create products')

    def create(self, **kwargs):
        try:
            instance = ProductsGenerator()
            products_list = instance.create_products()
            Product.objects.bulk_create(products_list)
            print('Populate products success')

        except Exception as e:
            print(f'Error ::: {e}')

    def handle(self, **options):
        self.create()