import logging
from datetime import datetime, date
from django.db import models, transaction
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.db.models import signals
from django.conf import settings
from django.dispatch import receiver
from base.models import BaseModel
from elasticsearch_app import ElasticSearchConnection


logger = logging.getLogger(__name__)


class People(BaseModel):
    name = models.CharField(_('Name'), max_length=255)
    cpf = models.CharField('CPF', max_length=14)
    rg = models.CharField('RG', max_length=12)
    birth_date = models.DateField(_('Birth date'))
    slug = AutoSlugField(populate_from='name', unique=True)
    sex = models.CharField(_('Sex'), choices=settings.SEX, max_length=9)
    sign = models.CharField(_('Sign'), max_length=15, choices=settings.SIGN)
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

# TODO Fix this property using correct logic.
    @property
    def age(self):
        try:
            born = datetime.strptime(self.birth_date, '%Y-%m-%d')

            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        except:
            born = self.birth_date
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @property
    def imc(self):
        return float(f'{self.weight / (self.height * self.height):.2f}')

    @property
    def weight_range(self):
        imc = self.imc
        label = 'obesity'
        if imc <= 18.5:
            label = 'under_weight'
        elif imc <= 24.9:
            label = 'right_weight'
        elif imc <= 29.9:
            label = 'overweight'

        return label

    @property
    def age_group(self):
        value = None
        age = int(self.age)
        if age <= 21:
            value = 'young'
        elif age < 65:
            value = 'adult'
        elif age >= 65:
            value = 'elderly'
        return value

    @property
    def all_fields(self):
        return sorted(vars(self).items())

    def absolute_url_api(self):
        return reverse('clients:people-detail', kwargs={'people_sid': self.uuid})


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

    logger.info(f'Try indexing:: {instance.pk} - {instance.name}')

    from clients.document import PeopleDocument

    try:
        with ElasticSearchConnection(PeopleDocument):
            document = PeopleDocument.build_document(instance=instance)
            document and document.save()
            logger.info(f'Indexing:: {instance.pk} - {instance.name} === SUCCESS')
            print(f'Indexing:: {instance.pk} - {instance.name} === SUCCESS')

    except Exception as e:
        logger.error(f'Indexing {instance.pk} - {instance.name} - FAIL.\nErro: {e}\n\n')
        print(f'Indexing {instance.pk} - {instance.name} - FAIL.\nErro: {e}\n\n')
