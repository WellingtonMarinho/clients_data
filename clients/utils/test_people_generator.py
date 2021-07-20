from django.test import TestCase
from .people_generator import ToPopulateDatabase

class TestPeopleGenerator(TestCase):
    def setUp(self) -> None:
        self.populate = ToPopulateDatabase()

    def test_sex_and_age(self):
        sex_and_age = self.populate.sex_and_age()
        assert sex_and_age[0] in 'FfMm'
        assert type(sex_and_age[1]) == int
        assert sex_and_age[1] > 17

    def test_parser_birth_date(self):
        content = [
            ('33/10/1333', '1333-10-33'),
            ('11/11/1111', '1111-11-11'),
            ('18/07/2021', '2021-07-18')
    ]
        for data, expected in content:
            with self.subTest():
                self.assertEqual(self.populate.parser_birth_date(data), expected)

    def test_replace_comma_to_dot(self):
        content = [
            ('1,78', '1.78'),
            ('1,85', '1.85'),
            ('1,75', '1.75'),
        ]
        for comma, dot in content:
            with self.subTest():
                self.assertEqual(self.populate.replace_comma_to_dot(comma), float(dot))

    def test_build_people(self):
        result = self.populate.build_people().keys()
        expected = ['name', 'cpf', 'rg', 'birth_date', 'sex', 'sign', 'mother_name',
                    'father_name', 'email', 'telefone_number', 'mobile', 'height',
                    'weight', 'type_blood', 'favorite_color']

        self.assertEqual(set(result), set(expected))
