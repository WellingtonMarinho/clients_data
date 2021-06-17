import django_filters.rest_framework
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_app import ElasticSearchConnection
from elasticsearch_app.paginator import DSEPaginator
from .document import PeopleSearch, PeopleDocument
from .models import People
from .serializers import PeopleSerializer, PeopleSearchSerializer

#
# class PeopleView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#     # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name', 'sign']

class PeopleView(APIView):

    def get(self, request):
        peoples = People.objects.all()
        print(peoples)
        print()
        print()
        serializer = PeopleSerializer(peoples, many=True)
        return Response(serializer.data)



class SearchPeopleView(APIView):

    def get(self, request, query):

        with ElasticSearchConnection(PeopleDocument):
            qs = PeopleSearch(query)
            response = qs.execute()

        data = [{
            'id': people.id,
            'name': people.name,
            'age':people.age,
            'cpf':people.cpf,
            'slug':people.slug,
            'birth_date':people.birth_date,
            'age_group':people.age_group,
            'sex':people.sex,
            'sign':people.sign,
            'mother_name':people.mother_name,
            'father_name':people.father_name,
            'email':people.email,
            'telefone_number':people.telefone_number,
            'mobile':people.mobile,
            'height':people.height,
            'weight':people.weight,
            'imc':people.imc,
            'type_blood':people.type_blood,
            'favorite_color':people.favorite_color,
                 } for people in response]


        serializer = PeopleSearchSerializer(data, many=True)

        return Response(serializer.data)
