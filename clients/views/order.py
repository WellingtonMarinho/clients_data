from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product
from clients.serializers.order import OrderSerializer, OrderProductSerializer, ProductSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateOrder(APIView):
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Order.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
