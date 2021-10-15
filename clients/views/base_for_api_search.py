from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clients.utils import BasicPagination, PaginationHandlerMixin
from elasticsearch_app import ElasticSearchConnection
from clients.utils.exceptions import ElasticSearchDocumentNotFound, ElasticSearchEngineClassNotFound
from clients.utils.validators import (validation_max_results, validation_boolean, validation_format_date,
                                      validation_sex_choice, validation_age_group)


class BaseElasticAPIView(PaginationHandlerMixin, APIView):
    serializer_class = None
    serializer_list_class = None
    pagination_class = BasicPagination
    model = None
    elastic_sort = ['_score', '-search_boost']
    elastic_search_document = None
    elastic_search_engine_class = None
    open_api_documentation = None

    def search_params(self, request, **kwargs):
        return dict(
            query=request.GET.get('q'),
            filters={'active': validation_boolean(request.GET.get('boolean', None), 'active')},
            sort=self.elastic_sort,
            created_at=validation_format_date(request.GET.get('created_at', None), 'created_at'),
            modified_at=validation_format_date(request.GET.get('modified_at', None), 'modified_at'),
            age_group=validation_age_group(request.GET.get('age')),
            sex=validation_sex_choice(request.GET.get('sex')),

            params=None,
        )

    def detail(self, args, **kwargs):
        assert self.model is not None, "BaseElasticAPIView detail requires a definition of model."
        assert self.serializer_class is not None, "BaseElasticAPIView Detail requires a definition of serializer."

        slug = args

        try:
            instance = self.model.objects.get(slug=slug)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)

        except Exception as e:
            return Response(data={
                'error': 'NotFound',
                'msg': e
            }, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        if self.elastic_search_document is None:
            raise ElasticSearchDocumentNotFound(
                "BaseElasticAPIView requires a definition of "
                "'elastic_document'")
        if self.elastic_search_engine_class is None:
            raise ElasticSearchEngineClassNotFound(
                "BaseElasticAPIView requires a definition of "
                "'elastic_document'")

        start = int(request.GET.get('start', 0))
        max_results = int(request.GET.get('limit_per_query', self.pagination_class.max_page_size))
        start, max_results = validation_max_results(start, max_results)

        with ElasticSearchConnection(self.elastic_search_document):
            query = self.elastic_search_engine_class(
                **self.search_params(request),
            )
            queryset = query[start:max_results].execute()

        serializer = self.create_serializer_paginated(queryset, self.serializer_list_class)

        return Response(serializer.data)

    def get(self, request):
        pass
