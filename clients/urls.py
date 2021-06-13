from django.urls import path

from clients.views import PeopleView


urlpatterns = [
    path('', PeopleView.as_view(), name='list-people'),
]