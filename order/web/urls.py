from django.urls import path
from .views import OrderView


app_name = 'order:web'

urlpatterns = [
    path('orders/', OrderView.as_view())
]