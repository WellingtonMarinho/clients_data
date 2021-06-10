from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import signals
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        abstract = True


class People(BaseModel):
    SEX = (
        ('f', 'Feminino'),
        ('m', 'Masculino'),
        # ('f', _('Female')),
        # ('m', _('Male'))
    )
    name = models.CharField(_('Name'), max_length=255)
    age = models.IntegerField(_('age'))
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=12)
    birth_date = models.DateField(_('Birth date'))
    sex = models.CharField(_('Sex'), choices=SEX, max_length=1)
    sign = models.CharField(max_length=15)
    mother_name = models.CharField(_('Mother Name'), max_length=255)
    father_name = models.CharField(_('Father Name'), max_length=250)
    email = models.EmailField('Email')
    telefone_number = models.CharField(_('Phone number'), max_length=20)
    mobile = models.CharField(_('Mobile'), max_length=20)
    height = models.FloatField(_('Height'))
    weight = models.IntegerField(_('Weight'))
    type_blood = models.CharField(_('Type blood'), max_length=3)
    favorite_color = models.CharField(_('Favorite color'), max_length=20)

    def __str__(self):
        return self.name


@receiver(signals.post_save, sender=People)
# @on_transaction_commit
def people_index(sender, instance, created, **kwargs):
    pass
    # from elasticsearch.document import PeopleDocument

    # try:
    #     with Elasti