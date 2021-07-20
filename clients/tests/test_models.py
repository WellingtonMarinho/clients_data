from django.test import TestCase

from clients.models import People


class ModelsPeopleTest(TestCase):
    def setUp(self):
        self.people = People.objects.create(
            name='José Joaquim Rafael Baptista',
            # age=33,
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
            ('2000-04-09', 'young'),
            ('2015-04-22', 'young'),
            ('1998-04-22', 'adult'),
            ('1975-04-22', 'adult'),
            ('1945-04-22', 'elderly'),
            ('1955-04-22', 'elderly'),
        ]
        for age, expected in contents:
            with self.subTest():
                self.people.birth_date = age
                self.assertEqual(self.people.age_group, expected)

    def test_imc_property(self):
        imc = self.people.imc
        expected = f'{self.people.weight / (self.people.height * self.people.height):.2f}'
        self.assertEqual(imc, float(expected))

    def test_weight_range_property(self):
        contents = [
            (50, 'under_weight'),
            (65, 'right_weight'),
            (74, 'overweight'),
            (83, 'obesity'),
        ]
        for weight, expected in contents:
            with self.subTest():
                self.people.weight = weight
                self.assertEqual(self.people.weight_range, expected)
