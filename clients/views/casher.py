from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order
from clients.serializers.casher import CasherSerializer


class CasherView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CasherSerializer
