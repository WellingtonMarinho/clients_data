from django.urls import path
from clients.views import ElasticSearchPeopleView, ProductView, OrderView


urlpatterns = [
    # path('orders/', CreateOrder.as_view(), name='order'),
    path('orders/', OrderView.as_view(), name='order'),
    path('products/', ProductView.as_view(), name='products'),
    path('elastic/', ElasticSearchPeopleView.as_view(), name='search'),
]
