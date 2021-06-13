from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import People
from fordev.validators import is_valid_cpf


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = [
            'name',
            'age',
            'cpf',
            'rg',
            'birth_date',
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
            'imc',
            'type_blood',
            'favorite_color',
        ]

    def validate_name(self, obj):
        if not obj.replace(' ', '').isalpha():
            raise ValidationError('Campo nome não pode conter números ou caracteres especiais.')
        return obj.title()

    def validate_cpf(self, obj):
        if is_valid_cpf(obj):
            return obj
        raise ValidationError('CPF não é válido.')
