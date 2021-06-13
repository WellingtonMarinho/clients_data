from django.urls import path

from clients.views import PeopleView,SearchPeopleView


urlpatterns = [
    path('', PeopleView.as_view(), name='list-people'),
    path('pesquise/<str:query>/', SearchPeopleView.as_view(), name='search')
]