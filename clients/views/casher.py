from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product
from clients.serializers.casher import CasherSerializer, ProductSerializer

