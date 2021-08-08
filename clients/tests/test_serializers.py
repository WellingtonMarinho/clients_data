from django.test import TestCase

from clients.models import People
from clients.serializers import PeopleSerializer
from rest_framework.exceptions import ValidationError

class SerializerPeopleCreateTest(TestCase):
    def setUp(self):
        self.people_data_dict = {
            "name": "José Joaquim Rafael Baptista",
            "cpf": "164.401.906-01",
            "rg": "10.805.637-5",
            "birth_date": "1988-04-22",
            "sex": "Masculino",
            "sign": "Touro",
            "mother_name": "Isabelle Sônia Aurora",
            "father_name": "Fernando Otávio Baptista",
            "email": "josejoaquimrafaelbaptista_@hoatmail.com",
            "telefone_number": "() 3587-4455",
            "mobile": "() 98132-5827",
            "height": 1.65,
            "weight": 50,
            "type_blood": "B-",
            "favorite_color": "preto"
        }
        self.serializer_create = PeopleSerializer(instance=self.people_data_dict)

        self.people_object = People.objects.create(**self.people_data_dict)

    def test_contains_expected_fields_in_serializer_create(self):
        result = self.serializer_create.data
        expected = [
                'name',
                'cpf',
                'rg',
                'birth_date',
                'sex',
                'sign',
                'mother_name',
                'father_name',
                'email',
                'telefone_number',
                'mobile',
                'height',
                'weight',
                'type_blood',
                'favorite_color'
            ]
        self.assertEqual(set(result.keys()), set(expected))

    def test_validate_cpf_raise_exception(self):
        falses_cpfs = ['789.416.310-99', '361.587.820-06', 'asadhfpad']
        for cpf in falses_cpfs:
            with self.subTest():
                self.assertRaises(ValidationError, self.serializer_create.validate_cpf, cpf)

    def test_validate_cpf_returns_true(self):
        cpfs = ['861.909.480-73', '290.846.610-44', '671.469.010-09']
        for cpf in cpfs:
            with self.subTest():
                self.assertTrue(self.serializer_create.validate_cpf(cpf))

    def test_validate_rg_returns_false(self):
        false_rgs = ['12.280.322-6', '71.356.879-4', '28.910.235-8', '43.687.796-7']
        for rg in false_rgs:
            with self.subTest():
                self.assertRaises(ValidationError, self.serializer_create.validate_rg, rg)

    def test_validate_rg_retuns_true(self):
        rgs = ['42.662.620-5', '32.240.472-1', '14.007.985-3', '15.519.735-6']
        for rg in rgs:
            with self.subTest():
                self.assertTrue(self.serializer_create.validate_rg(rg))

    def test_validate_name(self):
        names = ['wellington marinho soares', 'WELLINGTON MARINHO SOARES', 'weLLINGton maRINho soAREs']
        expected = 'Wellington Marinho Soares'
        for name in names:
            with self.subTest():
                self.assertEqual(self.serializer_create.validate_name(name), expected)
