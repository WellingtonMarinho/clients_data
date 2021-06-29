from django.urls import path
from clients.views import ElasticSearchPeopleView


urlpatterns = [
    path('', ElasticSearchPeopleView.as_view(), name='search'),
]

