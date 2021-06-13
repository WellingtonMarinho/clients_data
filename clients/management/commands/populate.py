from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from clients.generator import create_people


class Command(BaseCommand):
    help = _('Populate database')

    def create(self, **kwargs):
        try:
            for _ in range(2000):
                create_people()
                # print(_)
            print('Populate success')
        except Exception as e:
            print(f'Error ao popular banco de dados: \n\n{e}')

    def handle(self, **options):
        self.create()
