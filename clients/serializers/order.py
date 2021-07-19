from rest_framework import serializers
from clients.models import Order, Product, OrderProduct
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class OrderProductSerializer(WritableNestedModelSerializer, serializers.Serializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order

        fields = '__all__'
        depth = 0

    def create(self, validated_data):
        order_products = validated_data.pop('products', None)
        order = super().create(validated_data)

        for product in order_products:
            OrderProduct.objects.create(order=order, **product)

        return order















