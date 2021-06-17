import django_filters.rest_framework
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_app import ElasticSearchConnection
from elasticsearch_app.paginator import DSEPaginator
from .document import PeopleSearch, PeopleDocument
from .models import People
from .serializers import PeopleSerializer


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

        paginator = DSEPaginator(response, 25)
        queryset = paginator.page(1)

        # json = dumps(response[1])


        print()
        print()
        print(queryset)
        print()
        print(dir(queryset))
        print()
        print(queryset.__dict__)
        print()
        # print(dir(response))
        # print()
        # print()
        # print(response.facets)
        # print()
        # print()
        # print(response[1].name)
        # print()
        # print()
        # print(dir(response[1]))
        # print()
        # print()
        # print(type(response[1]))
        # print('#-#'*255)
        # print(json)
        # print('#-#'*255)

        print()
        print()
        print()
        print()
        return Response(queryset)