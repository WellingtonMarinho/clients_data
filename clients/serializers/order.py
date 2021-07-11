from rest_framework import serializers
from clients.models import Order, Product, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    items = OrderProductSerializer(many=True, source='products')

    class Meta:
        model = Order
        fields = [
            'id',
            'client',
            'created_at',
            'items'
        ]
