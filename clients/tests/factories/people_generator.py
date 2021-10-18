from fordev.generators import people
from clients.models import People
from random import randint, choices


class PeopleGenerator:
    def sex_and_age(self):
        SEX = ['F', 'M']
        sex = choices(SEX)[0]
        age = randint(18, 80)
        return sex, age

    def parser_birth_date(self, date):
        return '-'.join(list(reversed(date.split('/'))))

    def replace_comma_to_dot(self, str):
        return float(str.replace(',', '.'))

    def build_people(self):
        while True:
            sex, age = self.sex_and_age()
            data = people(sex=sex, age=age)
            people_dict = False
            try:
                if data['nome']:
                     people_dict = dict(
                        name=data['nome'],
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

                return people_dict

            except Exception as e:
                pass

    def build_list_of_people(self, number_of_peoples):
        try:
            list_people = []
            for each in range(number_of_peoples):
                people = self.build_people()
                if people:
                    data = People(**people)
                    list_people.append(data)
                    print(each, people['name'])

            return list_people

        except Exception as e:
            print(f'Error in build_list_of_people ::: {e}')
    
    def save_people(self):
        try:
            data = self.build_people()
            people = People.objects.create(**data)
        
            return people.save()
            
        except Exception as e:
            print(f'Error save_people ::: {e}')
