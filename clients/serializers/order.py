from rest_framework import serializers
from clients.models import Order, Product, OrderProduct
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        # fields = ['id', 'order', 'product', 'quantity']
        fields = '__all__'

        depth = 1


class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    products = OrderProductSerializer(many=True)



    class Meta:
        model = Order
        # fields = [
            # 'id',
            # 'client',
            # 'created_at',
            # 'products'
        # ]
        fields = '__all__'
        depth = 0