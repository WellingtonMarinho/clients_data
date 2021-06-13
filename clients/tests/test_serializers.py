from django.test import TestCase
from clients.serializers import PeopleSerializer
from rest_framework.exceptions import ValidationError

class SerializerPeopleCreateTest(TestCase):
    def setUp(self):
        self.people = {
            "name": "José Joaquim Rafael Baptista",
            "age": 33,
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
        self.serializer = PeopleSerializer(instance=self.people)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set([
                'name',
                'age',
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
            ]))

    def test_validate_cpf_returns_false(self):
        falses_cpfs = ['789.416.310-99', '361.587.820-06', 'asadhfpad']
        for cpf in falses_cpfs:
            with self.subTest():
                self.assertRaises(ValidationError, self.serializer.validate_cpf, cpf)

    def test_validate_cpf_returns_true(self):
        cpfs = ['861.909.480-73', '290.846.610-44', '671.469.010-09']
        for cpf in cpfs:
            with self.subTest():
                self.assertTrue(self.serializer.validate_cpf(cpf))

















