from django.test import TestCase
from django.conf import settings
from clients.models import People
from clients.serializers import PeoplePostSerializer, PeopleGetSerializer
from rest_framework.exceptions import ValidationError


class SerializerPeopleCreateTest(TestCase):
    def setUp(self):
        self.people_data_dict = {
            'name': 'Clarice Renata Alessandra Melo',
            'cpf': '369.624.702-23',
            'rg': '24.436.383-3',
            'birth_date': '1959-06-14',
            'sex': 'Feminino',
            'sign': 'Gêmeos',
            'mother_name': 'Isabelle Aurora Natália',
            'father_name': 'Bernardo Leandro Antonio Melo',
            'email': 'cclaricerenataalessandramelo@plastic.com.br',
            'telefone_number': '() 2972-8401',
            'mobile': '() 98106-4741',
            'height': 1.73,
            'weight': 83,
            'type_blood': 'B+',
            'favorite_color': 'amarelo'
        }

        self.people_object = People.objects.create(**self.people_data_dict)

        self.serializer_create = PeoplePostSerializer(instance=self.people_data_dict)


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

    def test_validate_name(self):
        names = ['wellington marinho soares', 'WELLINGTON MARINHO SOARES', 'weLLINGton maRINho soAREs']
        expected = 'Wellington Marinho Soares'
        for name in names:
            with self.subTest():
                self.assertEqual(self.serializer_create.validate_name(name), expected)

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

    def test_validate_sign_contains_in_settings_variable(self):
        signs = [sign[0] for sign in settings.SIGN]
        for sign in signs:
            with self.subTest():
                self.assertEqual(self.serializer_create.validate_sign(sign), sign)

    def test_validate_sign_raise_expection_if_sign_is_not_in_settings_variable(self):
        signs = ['Whatever', 'Again Whatever', 'Signs']
        for sign in signs:
            with self.subTest():
                self.assertRaises(ValidationError, self.serializer_create.validate_sign, sign)


class SerializerPeopleRetrieveTest(TestCase):
    def setUp(self):
        self.people_data_dict = {
            'name': 'Rebeca Heloise Lima',
            'cpf': '683.109.941-68',
            'rg': '36.229.184-6',
            'birth_date': '1981-05-03',
            'sex': 'Feminino',
            'sign': 'Touro',
            'mother_name': 'Marcela Eduarda Priscila',
            'father_name': 'Otávio Thales Lima',
            'email': 'rebecaheloiselima__rebecaheloiselima@mantegassi.com',
            'telefone_number': '() 3888-0907',
            'mobile': '() 99363-4068',
            'height': 1.63,
            'weight': 61,
            'type_blood': 'O+',
            'favorite_color': 'vermelho'
        }

        self.people_object = People.objects.create(**self.people_data_dict)

        self.serializer_retrieve = PeopleGetSerializer(instance=self.people_object)

    def test_contains_expected_fields_in_serializer_retrieve(self):
        expected = [
            'id',
            'name',
            'age',
            'cpf',
            'rg',
            'slug',
            'age_group',
            'sex',
            'sign',
            'mother_name',
            'father_name',
            'email',
            'telefone_number',
            'mobile',
            'height',
            'weight',
            'weight_range',
            'imc',
            'type_blood',
            'favorite_color',
            'absolute_url_api'
        ]
        result = self.serializer_retrieve.data
        self.assertEqual(set(expected), set(result.keys()))
