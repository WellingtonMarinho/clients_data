from django.test import TestCase

from clients.models import People


class ModelsPeopleTest(TestCase):
    def setUp(self):
        self.people = People.objects.create(
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

    def test_str(self):
        self.assertEqual(str(self.people), 'José Joaquim Rafael Baptista')

    def test_create(self):
        self.assertTrue(People.objects.exists())
        self.assertEqual(1, People.objects.count())

    def test_age_group(self):
        contents = [
            (19, 'Young'),
            (20, 'Young'),
            (26, 'Adult'),
            (64, 'Adult'),
            (66, 'Elderly'),
            (70, 'Elderly'),
        ]
        for age, expected in contents:
            with self.subTest():
                self.people.age = age
                self.assertEqual(self.people.age_group, expected)

    def test_imc_property(self):
        imc = self.people.imc
        expected = f'{self.people.weight / (self.people.height * self.people.height):.2f}'
        self.assertEqual(imc, expected)

















