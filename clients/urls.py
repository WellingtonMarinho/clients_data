from django.urls import path
from clients.views import ElasticSearchPeopleView, ProductView, OrderView, OrderProductView, ProductDetailView

urlpatterns = [
    # path('orders/', CreateOrder.as_view(), name='order'),
    path('orders/', OrderView.as_view(), name='order'),
    path('order-products/', OrderProductView.as_view(), name='order_product'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('elastic/', ElasticSearchPeopleView.as_view(), name='search'),
]
