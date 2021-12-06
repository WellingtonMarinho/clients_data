from django.urls import path, register_converter
from clients.views import PeopleAPIView, PeopleDetailAPIView, PeopleOrderAPIView
from clients.web.views import PeopleView
from base.utils import SID2UUIDConverter


register_converter(SID2UUIDConverter, 'sid')

app_name = 'clients'


urlpatterns = [
    path('people/', PeopleAPIView.as_view(), name='people-search'),
    path('<sid:people_sid>/', PeopleDetailAPIView.as_view(), name='people-detail'),
    path('', PeopleView.as_view(), name='people-list'),
    path('<int:people_id>/orders/', PeopleOrderAPIView.as_view(), name='people-orders')
]
