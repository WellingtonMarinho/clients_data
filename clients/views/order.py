from rest_framework import viewsets, generics, status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product, OrderProduct
from clients.serializers.order import OrderSerializer, OrderProductSerializer, ProductSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class CreateOrder(mixins.CreateModelMixin, GenericAPIView):
#     serializer_class = OrderProductSerializer
#
#     def get(self, request):
#         queryset = OrderProduct.objects.all().order_by('-id')
#         serializer = self.serializer_class(queryset, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
