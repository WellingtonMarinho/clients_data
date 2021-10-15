from rest_framework import serializers
from clients.models import OrderItems, Order, Product
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):
    absolute_url_api = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    def get_absolute_url_api(self, obj):
        return obj.absolute_url_api()

class OrderItemsSerializer(serializers.ModelSerializer):
    produto = ProductSerializer()

    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']


class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    items = OrderItemsSerializer(many=True, allow_null=True, )

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']


class PedidoPOSTSerializer(WritableNestedModelSerializer):
    items = OrderItemsPOSTSerializer(many=True, allow_null=True, )

    class Meta:
        model = Order
        fields = '__all__'
