from django.urls import path
from django.views.generic import TemplateView


from clients.views import ElasticSearchPeopleView

urlpatterns = [
    path('', ElasticSearchPeopleView.as_view(), name='search'),

]

