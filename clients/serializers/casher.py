from rest_framework import serializers

from clients.models import Order, Product

class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # price = serializers.DecimalField(max_digits=8, decimal_places=2)
    # description = serializers.CharField()
    class Meta:
        model = Product
        fields = '__all__'

class CasherSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = '__all__'