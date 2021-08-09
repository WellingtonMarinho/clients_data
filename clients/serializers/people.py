from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from clients.models import People
from fordev.validators import is_valid_cpf, is_valid_rg


class PeoplePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = [
            'name',
            'cpf',
            'rg',
            'slug',
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

    def validate_sign(self, obj):
        if obj in [sign[0] for sign in settings.SIGN]:
            return obj
        raise ValidationError('Signo inválido.')


class PeopleGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    search_boost = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(read_only=True)
    cpf = serializers.CharField(max_length=14)
    rg = serializers.CharField(max_length=12)
    slug = serializers.SlugField(read_only=True)
    age_group = serializers.CharField(read_only=True)
    sex = serializers.CharField(max_length=9)
    sign = serializers.CharField(max_length=15)
    mother_name = serializers.CharField(max_length=255)
    father_name = serializers.CharField(max_length=250)
    email = serializers.EmailField()
    telefone_number = serializers.CharField(max_length=20)
    mobile = serializers.CharField(max_length=20)
    height = serializers.FloatField()
    weight = serializers.IntegerField()
    weight_range = serializers.CharField(read_only=True)
    imc = serializers.FloatField(read_only=True)
    type_blood = serializers.CharField(max_length=3)
    favorite_color = serializers.CharField(max_length=20)
