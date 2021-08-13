from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from elasticsearch_app import ElasticSearchConnection
from clients.document import PeopleSearch, PeopleDocument
from clients.serializers import PeopleGetSerializer, PeoplePostSerializer
from clients.models import People
from clients.utils import BasicPagination, PaginationHandlerMixin, people_generator
from clients_data.settings import ELASTICSEARCH_PEOPLE_VIEW_OPENAPI


class PeopleView(PaginationHandlerMixin, APIView):
    serializer_class = PeopleGetSerializer
    pagination_class = BasicPagination

    def get_object(self, slug):
        try:
            return People.objects.get(slug=slug)
        except:
            raise Http404

    @extend_schema(parameters=ELASTICSEARCH_PEOPLE_VIEW_OPENAPI)
    def get(self, request):
        slug = request.GET.get('people', None)
        if slug:
            people = self.get_object(slug)
            serializer = PeopleGetSerializer(people)
            if serializer:
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        q = request.GET.get('q')
        max_results_per_query = int(request.GET.get('limit_per_query', self.pagination_class.max_page_size))
        start = int(request.GET.get('start', 0))
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))

        age_group = request.GET.getlist('age')
        sex = request.GET.getlist('sex')
        favorite_color = request.GET.getlist('favorite_color')
        weight_range = request.GET.getlist('weight_range')

        with ElasticSearchConnection(PeopleDocument):
            qs = PeopleSearch(q,
                filters={
                    'age_group': age_group,
                    'favorite_color': favorite_color,
                    'sex': sex,
                    'weight_range': weight_range,
                },
                sort=['_score', '-search_boost']
            )

            queryset = qs[start:max_results_per_query].execute()

        serializer = self.create_serializer_paginated(queryset)

        return Response(serializer.data)

    def post(self, request):
        serializer = PeoplePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
