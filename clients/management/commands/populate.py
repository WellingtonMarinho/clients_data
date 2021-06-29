from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from clients.generator import PopulateDatabase


class Command(BaseCommand):
    help = _('Populate database')

    def create(self, **kwargs):
        try:
            for _ in range(50000):
                try:
                    people = PopulateDatabase()
                    people.create_people()
                    print(f'Create object number {_}')
                except Exception as e:
                    pass
                
            print('Populate success')
        except Exception as e:
            print(f'Error ao popular banco de dados: \n\n{e}')

    def handle(self, **options):
        self.create()
