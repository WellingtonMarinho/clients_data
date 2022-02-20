from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from order.models import Product, Order
from order.serializers import OrderSerializer, ProductSerializer, OrderPOSTSerializer
from base.utils import PaginationHandlerMixin, BasicPagination


class OrderDetailAPIView(APIView):
    pass


class OrderAPIView(PaginationHandlerMixin, APIView):
    serializer_class = OrderSerializer
    pagination_class = BasicPagination

    def get_serializer_class(self, request):
        if request.method == "GET":
            return OrderSerializer
        else:
            return OrderPOSTSerializer

    @extend_schema(responses=serializer_class)
    def get(self, request):
        queryset = Order.objects.all().order_by('-id')
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated(serializer=self.get_serializer_class(request), queryset=queryset)
        return Response(serializer.data)

    @extend_schema(request=OrderPOSTSerializer)
    def post(self, request):
        serializer_class = self.get_serializer_class(request)
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductAPIView(PaginationHandlerMixin, APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = BasicPagination

    @extend_schema(responses=serializer_class)
    def get(self, request):
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated()
        return Response(serializer.data)

    @extend_schema(request=serializer_class)
    def post(self, request):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
