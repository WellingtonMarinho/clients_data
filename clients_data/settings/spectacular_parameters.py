from drf_spectacular.utils import OpenApiParameter


ELASTICSEARCH_PEOPLE_VIEW_OPENAPI = [
    OpenApiParameter(name='q', description='Search by name.'),
    OpenApiParameter(name='limit_per_query', description='Define limit to return objects.'),
    OpenApiParameter(name='start', description='Define initial number to slice queryset.'), # TODO Check english
    OpenApiParameter(name='end', description='Define limit to end slice queryset.'),
    OpenApiParameter(name='per_page', description='Define how many objects returns per page.'),
]
