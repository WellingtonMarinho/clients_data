from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product
from clients.serializers.order import OrderSerializer, OrderProductSerializer, ProductSerializer



class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

