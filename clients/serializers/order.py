from rest_framework import serializers

from clients.models import Order, Product, OrderProduct

class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # price = serializers.DecimalField(max_digits=8, decimal_places=2)
    # description = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # products = OrderProductSerializer(many=True, read_only=False)
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
