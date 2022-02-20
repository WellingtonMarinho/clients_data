import logging
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _ 
from clients.tests.factories.people_generator import PeopleGenerator


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = _('Populate Database and Elasticsearch')

    def create(self, **kwargs):
        try:
            for each in range(80):
                print(each)
                people = PeopleGenerator()
                people.save_people()
            print('Success in populate database.')
            logger.info('Success in populate database.')

        except Exception as e:
            logger.warning(e)
    

    def handle(self, **options):
        self.create()
    
