from django.urls import path
from clients.views import ElasticSearchPeopleView, OrderView


urlpatterns = [
    path('', OrderView.as_view(), name='order'),
    path('elastic', ElasticSearchPeopleView.as_view(), name='search'),
]
