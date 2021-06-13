from django.test import TestCase
# def _define_people_age(instance):
#     people_age = None
#     if instance.age < 25:
#         people_age = 'Young'
#     elif instance.age < 60:
#         people_age = 'Adult'
#     elif instance.age >= 60:
#         people_age = 'Elderly'
#
#     return people_age
#
# class Pessoa():
#     def __init__(self, age):
#         self.age = age
#
# p = Pessoa(60)
# result = _define_people_age(p)
# print(result)

indexes = {'default': [('index.peoples', 'clients.document.PeopleDocument')]}

for index, value in indexes.get('default'):
    print(index, value)
