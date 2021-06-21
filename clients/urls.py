from django.urls import path
from django.views.generic import TemplateView


from clients.views import PeopleView, SearchPeopleView, ElasticSearchSearchPeopleView

urlpatterns = [
    path('', PeopleView.as_view(), name='list-people'),
    path('elasticsearch/<str:query>/', ElasticSearchSearchPeopleView.as_view(), name='search'),
    path('postgres/<str:query>/', ElasticSearchSearchPeopleView.as_view(), name='search'),


    path('swagger-ui', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

