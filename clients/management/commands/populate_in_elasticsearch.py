import logging
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _ 
from clients.utils.people_generator import ToPopulateDatabase


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = _('Populate Database and Elasticsearch')

    def create(self, **kwargs):
        try:
            for each in range(200):
                print(each)
                people = ToPopulateDatabase()
                people.save_people()
            print('Success in populate database.')
            logger.info('Success in populate database.')

        except Exception as e:
            print('Erro ao executar comando')
    

    def handle(self, **options):
        self.create()
    