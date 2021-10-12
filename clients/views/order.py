from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.models import Order, Product, Pedido
# from clients.serializers.order import OrderSerializer, ProductSerializer, OrderToGetSerializer
from clients.serializers.order import ItensDoPedidoSerializer, PedidoSerializer, ProductSerializer
from clients.utils.api_pagination import PaginationHandlerMixin, BasicPagination


class OrderView(PaginationHandlerMixin, APIView):
    serializer_class = PedidoSerializer
    pagination_class = BasicPagination

    def get(self, request):
        queryset = Pedido.objects.all().order_by('-id')
        self.pagination_class.page_size = int(request.GET.get('per_page', self.pagination_class.page_size))
        serializer = self.create_serializer_paginated(serializer=PedidoSerializer, queryset=queryset)
        return Response(serializer.data)

    def post(self, request):
        print('####'*88)
        print(request.data)

        cliente = request.data.pop('cliente', None)
        itens = request.data.pop('items', None)
        product = request.data.pop('produto', None)
        if cliente and itens and product:
            print(request.data)
            serializer = self.serializer_class(data={'cliente': cliente})

            if serializer.is_valid():
                serializer.save()
                print(serializer.error)

            serializer = ItensDoPedidoSerializer(data={'items': itens})
            if serializer.is_valid():
                serializer.save()
                print(serializer.error)
            serializer = ProductSerializer(data={'produto': product})
            if serializer.is_valid():
                serializer.save()
                print(serializer.error)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'Error': 'Erro desconhecido'}, status.HTTP_400_BAD_REQUEST)

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
