from django.urls import path, register_converter
from order.views import (ProductAPIView, OrderAPIView, OrderDetailAPIView, ProductDetailAPIView)
from base.utils import SID2UUIDConverter


register_converter(SID2UUIDConverter, 'sid')

app_name = 'order:api'


urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order'),
    path('orders/<sid:order_sid>/', OrderDetailAPIView.as_view(), name='order-detail'),

    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<slug:product_slug>/', ProductDetailAPIView.as_view(), name='products-detail'),

]