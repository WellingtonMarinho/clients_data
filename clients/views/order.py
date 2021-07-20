from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product, OrderProduct
from clients.serializers.order import OrderSerializer, OrderProductSerializer, ProductSerializer, OrderToGetSerializer
from clients.utils.api_pagination import PaginationHandlerMixin, BasicPagination


class OrderView(PaginationHandlerMixin, APIView):
    queryset = Order.objects.all()
    serializer_class = OrderToGetSerializer
    pagination_class = BasicPagination
    pagination_class.page_size = 1

    def get(self, request):
        queryset = self.queryset
        page = self.paginate_queryset(queryset)

        if page:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)
        # serializer = self.create_serializer_paginated()
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
    pagination_class.page_size = 10

    def get(self, request):
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


# class OrderProductView(APIView):
#     queryset = OrderProduct.objects.all()
#     serializer_class = OrderProductSerializer
#
#     def get(self, request):
#         queryset = OrderProduct.objects.all()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)