import logging

from django.core.management.base import BaseCommand
from clients.management.commands.populate_in_elasticsearch import Command as populate_in_elasticsearch
from order.management.commands.create_products import Command as create_products
from order.management.commands.create_orders import Command as create_order


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def create(self):
        try:
            people = populate_in_elasticsearch()
            people.handle()
            logger.info('::: PEOPLE CREATEAD')

            product = create_products()
            product.handle()
            logger.info('::: PRODUCT CREATEAD')

            order = create_order()
            order.handle()
            logger.info('::: ORDER CREATEAD')

        except Exception as e:
            logger.debug(f'ERROR: {e}')

    def handle(self, **options):
        self.create()