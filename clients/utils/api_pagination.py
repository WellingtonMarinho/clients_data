from rest_framework.pagination import PageNumberPagination
from .exceptions import QuerySetNotFound, SerializerClassNotFound

class BasicPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5000


class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None # Ensures which the property by right,
        return self.paginator.get_paginated_response(data)

    # def create_serializer_paginated(self, queryset=None, serializer=None):
    #     """If class have queryset or/and serializer_class is not necessary make assign explicit"""
    #     if queryset is None:
    #         # if self.queryset is None:
    #         #     raise QuerySetNotFound('Queryset not found.')
    #         queryset = self.queryset
    #
    #     if serializer is None:
    #         # if self.serializer_class is None:
    #         #     raise SerializerClassNotFound('serializer_class not found.')
    #         serializer = self.serializer_class
    #
    #     page = self.paginate_queryset(queryset)
    #
    #     if page:
    #         serializer = self.get_paginated_response(serializer(page, many=True).data)
    #     else:
    #         serializer = serializer(queryset, many=True)
    #
    #     return serializer
