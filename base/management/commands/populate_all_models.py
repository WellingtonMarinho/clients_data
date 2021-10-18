from django.core.management.base import BaseCommand
from clients.management.commands.populate_in_elasticsearch import Command as populate_in_elasticsearch
from order.management.commands.create_products import Command as create_products
from order.management.commands.create_order import Command as create_order


class Command(BaseCommand):
    def create(self):
        try:
            people = populate_in_elasticsearch()
            people.handle()
            print('::: PEOPLE CREATEAD')
            product = create_products()
            product.handle()
            print('::: PRODUCT CREATEAD')
            order = create_order()
            order.handle()
            print('::: ORDER CREATEAD')

        except Exception as e:
            print(f'ERROR: {e}')

    def handle(self, **options):
        self.create()