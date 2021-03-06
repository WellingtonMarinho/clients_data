from django.conf import settings
from elasticsearch_dsl import (Document, FacetedSearch, Integer,
                               Keyword, Text, DateRange,
                               Search, TermsFacet, Long, Date)
from clients.models import People

from elasticsearch_app.analyzers import brazilian_text_analyzer
from elasticsearch_app import DocumentBase
from elasticsearch_app.faceted_search import CreateAndModifiedFacetedSearch


class PeopleDocument(DocumentBase):
    id = Long(required=True)
    name = Text(analyzer=brazilian_text_analyzer)
    name_keyword = Keyword()
    age = Integer()
    cpf = Keyword()
    rg = Keyword()
    birth_date = Date()
    age_group = Keyword()
    slug = Keyword()
    sex = Keyword()
    sign = Keyword()
    mother_name = Text(analyzer=brazilian_text_analyzer)
    father_name = Text(analyzer=brazilian_text_analyzer)
    email = Keyword()
    phone_number = Keyword()
    mobile = Keyword()
    height = Text()
    weight = Text()
    weight_range = Keyword()
    type_blood = Keyword()
    favorite_color = Keyword()

    class Index:
        name = settings.PROJECT_INDEX_PEOPLE
        settings = {
            "number_of_shards": 2
        }

    @classmethod
    def get_model(cls):
        return People

    @classmethod
    def build_document(cls, instance):
        """
        Here it's possible create a method for to search boost in attribute
        """
        """
        Implementar um facet por peso a critério de teste seria bacana
        Ex: calcular IMC, setar um field no document e facetar por magro, ideal, acima, obesidade
        """

        if instance.name:
            search_boost = cls._search_boost(instance)

            document = PeopleDocument(
                _id=instance.pk,
                id=instance.pk,
                name=instance.name,
                name_keyword=instance.name,
                age=instance.age,
                age_group=instance.age_group,
                slug=instance.slug,
                cpf=instance.cpf,
                rg=instance.rg,
                birth_date=instance.birth_date,
                sex=instance.sex,
                sign=instance.sign,
                mother_name=instance.mother_name,
                father_name=instance.father_name,
                email=instance.email,
                telefone_number=instance.telefone_number,
                mobile=instance.mobile,
                height=instance.height,
                weight=instance.weight,
                imc=instance.imc,
                weight_range=instance.weight_range,
                type_blood=instance.type_blood,
                favorite_color=instance.favorite_color,
                search_boost=search_boost,
                absolute_url_api=instance.absolute_url_api()
            )
            return document

    @classmethod
    def _search_boost(cls, instance):
        return 100 + instance.age



class PeopleSearch(CreateAndModifiedFacetedSearch):
# class PeopleSearch(FacetedSearch):
    index = PeopleDocument.Index.name
    doc_types = [PeopleDocument,]
    fields = ['name_keyword^100', 'name^10', 'sign']

    facets = {
        'age_group': TermsFacet(field='age_group.keyword'),
        'favorite_color': TermsFacet(field='favorite_color.keyword'),
        'sex': TermsFacet(field='sex.keyword'),
        'weight_range': TermsFacet(field='weight_range.keyword'),
    }
