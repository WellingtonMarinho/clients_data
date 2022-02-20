from django.urls import path
from order.web.views import OrderView


app_name = 'order:web'

urlpatterns = [
    path('orders/', OrderView.as_view())
]