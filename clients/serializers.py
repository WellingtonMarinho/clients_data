from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import People
from fordev.validators import is_valid_cpf, is_valid_rg


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = [
            'name',
            'age',
            'cpf',
            'rg',
            'slug',
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

    def validate_cpf(self, cpf):
        if is_valid_cpf(cpf):
            return cpf
        raise ValidationError('CPF não é válido.')

    def validate_rg(self, rg):
        if is_valid_rg(rg):
            return rg
        raise ValidationError('RG não é válido.')


class PeopleSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    search_boost = serializers.CharField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    cpf = serializers.CharField(max_length=14)
    rg = serializers.CharField(max_length=12)
    slug = serializers.SlugField()
    birth_date = serializers.DateTimeField()
    age_group = serializers.CharField()
    sex = serializers.CharField(max_length=9)
    sign = serializers.CharField(max_length=15)
    mother_name = serializers.CharField(max_length=255)
    father_name = serializers.CharField(max_length=250)
    email = serializers.EmailField()
    telefone_number = serializers.CharField(max_length=20)
    mobile = serializers.CharField(max_length=20)
    height = serializers.FloatField()
    weight = serializers.IntegerField()
    imc = serializers.FloatField()
    type_blood = serializers.CharField(max_length=3)
    favorite_color = serializers.CharField(max_length=20)
