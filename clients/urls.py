from django.urls import path, register_converter
from clients.views import PeopleAPIView, PeopleDetailAPIView
from base.utils import SID2UUIDConverter


register_converter(SID2UUIDConverter, 'sid')

app_name = 'clients'


urlpatterns = [
    path('', PeopleAPIView.as_view(), name='people-search'),
    path('<sid:people_sid>/', PeopleDetailAPIView.as_view(), name='people-detail'),
]
