from fordev.generators import people
from clients.models import People
from random import randint, choices

class ToPopulateDatabase():
    def sex_and_age(self):
        SEX = ['F', 'M']
        sex = choices(SEX)[0]
        age = randint(18, 80)
        return sex, age

    def parser_birth_date(self, date):
        return '-'.join(list(reversed(date.split('/'))))

    def replace_comma_to_dot(self, str):
        return float(str.replace(',', '.'))

    def create_people(self):
        sex, age = self.sex_and_age()
        data = people(sex=sex, age=age)
        person = People.objects.create(
            name=data['nome'],
            age=data['idade'],
            cpf=data['cpf'],
            rg=data['rg'],
            birth_date=self.parser_birth_date(data['data_nasc']),
            sex=data['sexo'],
            sign=data['signo'],
            mother_name=data['mae'],
            father_name=data['pai'],
            email=data['email'],
            telefone_number=data['telefone_fixo'],
            mobile=data['celular'],
            height=self.replace_comma_to_dot(data['altura']),
            weight=data['peso'],
            type_blood=data['tipo_sanguineo'],
            favorite_color=data['cor'],
        )
        return person

    def save(self):
        try:
            data = self.create_people()
            data.save()
        except Exception as e:
            print(f'Error ::: {e}')