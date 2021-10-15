from rest_framework import serializers
from clients.models import ItensDoPedido, Pedido, Product
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):
    absolute_url_api = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    def get_absolute_url_api(self, obj):
        return obj.absolute_url_api()

class ItensDoPedidoSerializer(serializers.ModelSerializer):
    produto = ProductSerializer()

    class Meta:
        model = ItensDoPedido
        fields = ['produto', 'quantidade']


class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    items = ItensDoPedidoSerializer(many=True, allow_null=True, )

    class Meta:
        model = Pedido
        fields = '__all__'


class ItensDoPedidoPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItensDoPedido
        fields = ['produto', 'quantidade']


class PedidoPOSTSerializer(WritableNestedModelSerializer):
    items = ItensDoPedidoPOSTSerializer(many=True, allow_null=True, )

    class Meta:
        model = Pedido
        fields = '__all__'
