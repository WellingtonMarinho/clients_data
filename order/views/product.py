from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from order.models import Product
from order.serializers import  ProductSerializer, ProductDetailSerializer


class ProductDetailAPIView(APIView):
    serializer_class = ProductDetailSerializer

    @extend_schema(request=serializer_class)
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
