from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from order.models import OrderItems, Order
from .products import ProductSerializer


class OrderItemsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItems
        fields = ['product', 'quantity', 'total_per_item']


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    items = OrderItemsSerializer(many=True, allow_null=True, )
    total_order = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_client(self, obj):
        return obj.client.absolute_url_api()


class OrderItemsPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']


class OrderPOSTSerializer(WritableNestedModelSerializer):
    items = OrderItemsPOSTSerializer(many=True, allow_null=True, )

    class Meta:
        model = Order
        fields = '__all__'
