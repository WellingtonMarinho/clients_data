from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from json import dumps, loads
from .document import PeopleSearch, PeopleDocument
from elasticsearch_app import ElasticSearchConnection
from elasticsearch_app.paginator import DSEPaginator

from .models import People
from .serializers import PeopleSerializer


class PeopleView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

