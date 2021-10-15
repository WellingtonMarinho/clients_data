from django.urls import path, register_converter
from clients.views import (PeopleAPIView, ProductAPIView, OrderAPIView, OrderDetailAPIView,
                           ProductDetailAPIView, PeopleDetailAPIView)
from clients.utils.converters import SID2UUIDConverter


register_converter(SID2UUIDConverter, 'sid')

app_name = 'api'

urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order'),
    path('orders/<sid:order_sid>/', OrderDetailAPIView.as_view(), name='order-detail'),

    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<slug:product_slug>/', ProductDetailAPIView.as_view(), name='products-detail'),

    path('people/', PeopleAPIView.as_view(), name='people-search'),
    path('people/<sid:people_sid>/', PeopleDetailAPIView.as_view(), name='people-detail'),
]
