from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from order.tests.factories import OrderGenerator


QUANTITY_OF_ORDERS = 150

class Command(BaseCommand):
    help = _('Create orders')

    def create(self, **kwargs):
        try:
            for _ in range(QUANTITY_OF_ORDERS):
                instance = OrderGenerator()
                instance.create_order()

            print('Populate success')

        except Exception as e:
            print(f'Error ::: {e}')

    def handle(self, **options):
        self.create()