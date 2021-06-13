from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.db.models import signals
from django.dispatch import receiver

from elasticsearch_app import ElasticSearchConnection


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        abstract = True


class People(BaseModel):
    SEX = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        # ('f', _('Female')),
        # ('m', _('Male'))
    )
    name = models.CharField(_('Name'), max_length=255)
    age = models.IntegerField(_('age'))
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=12)
    birth_date = models.DateField(_('Birth date'))
    sex = models.CharField(_('Sex'), choices=SEX, max_length=9)
    sign = models.CharField(max_length=15)
    mother_name = models.CharField(_('Mother Name'), max_length=255)
    father_name = models.CharField(_('Father Name'), max_length=250)
    email = models.EmailField('Email')
    telefone_number = models.CharField(_('Phone number'), max_length=20, blank=True, null=True)
    mobile = models.CharField(_('Mobile'), max_length=20)
    height = models.FloatField(_('Height'))
    weight = models.IntegerField(_('Weight'))
    type_blood = models.CharField(_('Type blood'), max_length=3)
    favorite_color = models.CharField(_('Favorite color'), max_length=20)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

    @property
    def imc(self):
        return f'{self.weight / (self.height * self.height):.2f}'

    @property
    def age_group(self):
        value = None
        age = int(self.age)
        if age <= 21:
            value = 'Young'
        elif age < 65:
            value = 'Adult'
        elif age >= 65:
            value = 'Elderly'
        return value

def on_transaction_commit(func):
    """
    Decorator to run signals only after transaction commit
    Example:

    @receiver(post_save, sender=SomeModel)
    @on_transaction_commit
    def my_ultimate_func(sender, **kwargs):
        # Do things here

    """
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner


@receiver(signals.post_save, sender=People)
@on_transaction_commit
def people_index(sender, instance, created, **kwargs):

    print(f'Try indexing:: {instance.pk} - {instance.name}')

    from .document import PeopleDocument

    try:
        with ElasticSearchConnection(PeopleDocument):
            document = PeopleDocument.build_document(instance=instance)
            print(f'DOCUMENT:::-> {document}')
            document and document.save()
            print(f'Indexing:: {instance.pk} - {instance.name} === SUCCESS')

    except Exception as e:
        print(f'Indexing {instance.pk} - {instance.name} - FAIL.\nErro: {e}\n\n')
