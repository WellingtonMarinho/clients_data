from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from order.models import Product, Order
from order.serializers.order import OrderSerializer, ProductSerializer, OrderPOSTSerializer
from clients.utils.api_pagination import PaginationHandlerMixin, BasicPagination


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

    def get(self, request):
        queryset = Order.objects.all().order_by('-id')
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated(serializer=self.get_serializer_class(request), queryset=queryset)
        return Response(serializer.data)

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


class ProductDetailAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, product_slug):

        if Product.objects.filter(slug=product_slug).exists():

            obj = Product.objects.get(slug=product_slug)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)

        return Response(
            data={'error': 'NotFound'},
            status=status.HTTP_404_NOT_FOUND
        )


class ProductDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product, id=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)

        return Response(serializer.data)
