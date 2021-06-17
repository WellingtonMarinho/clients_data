import django_filters.rest_framework
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_app import ElasticSearchConnection
from elasticsearch_app.paginator import DSEPaginator
from .document import PeopleSearch, PeopleDocument
from .models import People
from .serializers import PeopleSerializer, PeopleSearchSerializer


class PeopleView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'sign']


class SearchPeopleView(APIView):

    def get(self, request, query):

        with ElasticSearchConnection(PeopleDocument):
            qs = PeopleSearch(query)
            response = qs.execute()

        data = [{
            'name': people.name,
            'age':people.age,
            'cpf':people.cpf,
            'rg':people.rg,
                 } for people in response]
        serializer = PeopleSearchSerializer(data[0])

        return Response(serializer.data)
