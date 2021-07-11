from django.urls import path
from clients.views import ElasticSearchPeopleView, OrderView, ProductView, CreateOrder


urlpatterns = [
    path('orders/', CreateOrder.as_view(), name='order'),
    path('products/', ProductView.as_view(), name='order'),
    path('elastic/', ElasticSearchPeopleView.as_view(), name='search'),
]
