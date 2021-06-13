from fordev.generators import people
from .models import People
from random import randint, choices


def sex_and_age():
    SEX = ['F', 'M']
    sex = choices(SEX)[0]
    age = randint(18, 80)
    return sex, age

def parser_birth_date(date):
    return '-'.join(list(reversed(date.split('/'))))

def replace_comma_to_dot(str):
    return float(str.replace(',', '.'))

def create_people():
    sex, age = sex_and_age()
    data = people(sex=sex, age=age)
    person = People.objects.create(
        name=data['nome'],
        age=data['idade'],
        cpf=data['cpf'],
        rg=data['rg'],
        birth_date=parser_birth_date(data['data_nasc']),
        sex=data['sexo'],
        sign=data['signo'],
        mother_name=data['mae'],
        father_name=data['pai'],
        email=data['email'],
        telefone_number=data['telefone_fixo'],
        mobile=data['celular'],
        height=replace_comma_to_dot(data['altura']),
        weight=data['peso'],
        type_blood=data['tipo_sanguineo'],
        favorite_color=data['cor'],
    )
    person.save()
