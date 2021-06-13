from django.test import TestCase

from clients.models import People


class ModelsPeopleTest(TestCase):
    def setUp(self):
        people = People.objects.create(
            name='José Joaquim Rafael Baptista',
            age=33,
            cpf='164.401.906-01',
            rg='10.805.637-5',
            birth_date='1988-04-22',
            sex='Masculino',
            sign='Touro',
            mother_name='Isabelle Sônia Aurora',
            father_name='Fernando Otávio Baptista',
            email='josejoaquimrafaelbaptista_@hoatmail.com',
            telefone_number='() 3587-4455',
            height=1.65,
            weight=50,
            type_blood='B-',
            favorite_color='preto'
        )