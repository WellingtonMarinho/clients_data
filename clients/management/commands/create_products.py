from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from clients.utils.products_generator import ProductsGenerator
from clients.models import Product


class Command(BaseCommand):
    help = _('Create products')

    def create(self, **kwargs):
        try:
            instance = ProductsGenerator()
            products_list = instance.create_products()
            Product.objects.bulk_create(products_list)

        except Exception as e:
            print(f'ERROR: {e}')

    def handle(self, **options):
        self.create()