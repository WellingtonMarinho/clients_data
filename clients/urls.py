from django.urls import path
from clients.views import PeopleElasticSearchView, ProductView, OrderView, ProductDetailView

urlpatterns = [
    path('orders/', OrderView.as_view(), name='order'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('people/', PeopleElasticSearchView.as_view(), name='search'),
]
