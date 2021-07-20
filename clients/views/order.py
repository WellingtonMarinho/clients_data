from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product
from clients.serializers.order import OrderSerializer, ProductSerializer, OrderToGetSerializer
from clients.utils.api_pagination import PaginationHandlerMixin, BasicPagination


class OrderView(PaginationHandlerMixin, APIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    pagination_class = BasicPagination

    def get(self, request):
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated(serializer=OrderToGetSerializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(PaginationHandlerMixin, APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = BasicPagination

    def get(self, request):
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated()
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product, id=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)

        return Response(serializer.data)
