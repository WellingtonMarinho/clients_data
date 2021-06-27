from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_app import ElasticSearchConnection
from .document import PeopleSearch, PeopleDocument
from .serializers import PeopleSearchSerializer
from .pagination import BasicPagination, PaginationHandlerMixin


class ElasticSearchPeopleView(APIView, PaginationHandlerMixin):
    serializer_class = PeopleSearchSerializer
    pagination_class = BasicPagination

    def get(self, request):
        q = request.GET.get('q')

        with ElasticSearchConnection(PeopleDocument):
            qs = PeopleSearch(q,
                sort=['_score', '-search_boost']
            )
            response = qs.execute()
            print('#-#'*155)
            print(response)
            print(len(response))
            print('#-#'*155)

        page = self.paginate_queryset(response)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = PeopleSearchSerializer(response, many=True)

        return Response(serializer.data)
