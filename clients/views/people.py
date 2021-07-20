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
    pagination_class.page_size = 5
    # pagination_class.max_page_size = 20

    def get(self, request):
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
        page = self.paginate_queryset(queryset)

        if page:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)
        # serializer = self.create_serializer_paginated(queryset)

        return Response(serializer.data)
