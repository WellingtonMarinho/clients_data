from random import randint, choices
import factory
from factory.django import DjangoModelFactory
from django.conf import settings

faker = factory.faker.faker.Faker(['pt_BR'])
factory.faker.faker.Faker.seed(10)
SIGN = [sign[0] for sign in settings.SIGN]



class PeopleFactory(DjangoModelFactory):
    name = factory.Faker('name')
    cpf = factory.Faker('cpf', locale='pt_BR')
    email = factory.Faker('email')
    sex = factory.Iterator(['feminino', 'masculino'])
    sign = factory.lazy_attribute(lambda obj: )

