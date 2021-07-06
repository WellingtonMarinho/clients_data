from django.urls import path
from clients.views import ElasticSearchPeopleView, CasherView


urlpatterns = [
    path('', CasherView.as_view(), name='casher'),
    path('elasticsearch', ElasticSearchPeopleView.as_view(), name='search'),

]

