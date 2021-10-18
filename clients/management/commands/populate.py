from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from clients.utils.people_generator import ToPopulateDatabase
from clients.models import People


class Command(BaseCommand):
    help = _('Populate database')

    def create(self, **kwargs):
        try:
            people = ToPopulateDatabase()
            people_list = people.build_list_of_people(25)
            print('Bulk Create to Populate...')
            People.objects.bulk_create(people_list)
            print()
            print('Populate success!')

        except Exception as e:
            print(f'Error ao popular banco de dados: \n\n{e}')

    def handle(self, **options):
        self.create()
