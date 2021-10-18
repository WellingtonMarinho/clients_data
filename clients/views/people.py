from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from elasticsearch_app import ElasticSearchConnection
from clients.document import PeopleSearch, PeopleDocument
from clients.serializers import PeopleGetSerializer, PeoplePostSerializer
from clients.models import People
from base.utils import BasicPagination, PaginationHandlerMixin
from clients_data.settings import ELASTICSEARCH_PEOPLE_VIEW_OPENAPI
from base.utils import validation_age_group
from .base_for_api_search import BaseElasticAPIView


# class PeopleDetailAPIView(APIView):
#     serializer_class = PeopleGetSerializer
#
#     def get(self, request, people_slug):
#         print('***'*88)
#
#         if People.objects.filter(slug=people_slug).exists():
#             obj = People.objects.get(slug=people_slug)
#             serializer = self.serializer_class(obj)
#             return Response(serializer.data)
#
#         return Response(
#             data={'error': 'NotFound'},
#             status=status.HTTP_404_NOT_FOUND
#         )

#
class PeopleAPIView(BaseElasticAPIView):
    elastic_search_document = PeopleDocument
    elastic_search_engine_class = PeopleSearch
    serializer_class = PeopleGetSerializer

    def create_filters(self, request):
        filters = super().create_filters(request)
        custom_filters = {
            'weight_range': request.GET.get('weight_range'),
            'age_group': validation_age_group(request.GET.get('age')),
            'sex': request.GET.get('sex'),
            'favorite_color': request.GET.getlist('favorite_color')
        }
        filters.update(custom_filters)
        return filters

    def list(self, request):
        per_page = int(request.GET.get('per_page', self.pagination_class.page_size))
        self.pagination_class.page_size = per_page
        return super().list(request)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        serializer = PeoplePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleDetailAPIView(BaseElasticAPIView):
    serializer_class = PeopleGetSerializer
    model = People
    
    def get(self, request, people_sid):
        return self.detail(people_sid)

    # def get(self, request, people_slug):
    #     if People.objects.filter(slug=people_slug).exists():
    #
    #         people = People.objects.get(slug=people_slug)
    #         serializer = self.serializer_class(people)
    #         return Response(serializer.data)
    #
    #     return Response(
    #         data={'error': 'NotFound'},
    #         status=status.HTTP_404_NOT_FOUND
    #     )
