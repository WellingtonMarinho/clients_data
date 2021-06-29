from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from elasticsearch_app import ElasticSearchConnection
from clients.document import PeopleSearch, PeopleDocument
from clients.serializers import PeopleSearchSerializer
from clients.utils import BasicPagination, PaginationHandlerMixin
from clients_data.settings import ELASTICSEARCH_PEOPLE_VIEW_OPENAPI


@extend_schema(parameters=ELASTICSEARCH_PEOPLE_VIEW_OPENAPI)
class ElasticSearchPeopleView(APIView, PaginationHandlerMixin):
    serializer_class = PeopleSearchSerializer
    pagination_class = BasicPagination
    pagination_class.page_size = 20

    def get(self, request):
        q = request.GET.get('q')

        max_results_per_query = int(request.GET.get('limit_per_query', self.pagination_class.max_page_size))
        start = int(request.GET.get('start', 0))
        end = int(request.GET.get('end', max_results_per_query))
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        people_age = 'Adult'
        sex = 'Feminino'

        with ElasticSearchConnection(PeopleDocument):
            qs = PeopleSearch(q,
                filters={
                    'people_age': people_age,
                    # 'sex': sex
                },
                sort=['_score', '-search_boost']
            )

            queryset = qs[start:end].execute()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
