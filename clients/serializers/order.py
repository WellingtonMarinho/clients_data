from rest_framework import serializers
from clients.models import ItensDoPedido, Pedido, Product, People


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class ItensDoPedidoSerializer(serializers.ModelSerializer):
    # produto = serializers.StringRelatedField()
    produto = ProductSerializer()


    class Meta:
        model = ItensDoPedido
        fields = ['id', 'produto', 'quantidade']


class PedidoSerializer(serializers.ModelSerializer):
    # cliente = serializers.StringRelatedField()
    # items = ItensDoPedidoSerializer(many=True, allow_null=True, )
    # produto = ProductSerializer(many=True, allow_null=True)


    class Meta:
        model = Pedido
        fields = '__all__'
    #
    # def create(self, validated_data):
    #         print('***'*88)
    #         print()
    #         # print(validated_data, 'HERE')
    #         # print()
    #         # print(dir(validated_data))
    #
    #
    #         order_products = validated_data.pop('items', None)
    #         print(order_products, 'order_products')
    #         print(dir(order_products), 'order_products')
    #
    #         id_people = validated_data.pop('cliente', None)
    #         order = Pedido.objects.create(cliente=id_people)
    #
    #         for product in order_products:
    #             print(product)
    #             print(dir(product))
    #             ItensDoPedido.objects.create(pedido=order, **product)
    #
    #         return order


# from rest_framework import serializers
# from clients.models import Order, Product, OrderProduct
# from drf_writable_nested import WritableNestedModelSerializer
#
#
#
# class OrderProductSerializer(WritableNestedModelSerializer, serializers.Serializer):
#     class Meta:
#         model = OrderProduct
#         fields = ['product', 'quantity']
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     products = OrderProductSerializer(many=True)
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#         depth = 0
#
#     def create(self, validated_data):
#         print('***'*88)
#         print()
#         print()
#         print(validated_data)
#         print()
#         print(type(validated_data))
#         order_products = validated_data.pop('products', None)
#         order = super().create(validated_data)
#
#         for product in order_products:
#             OrderProduct.objects.create(order=order, **product)
#
#         return order
#
#
# # class OrderProductToGetSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = OrderProduct
# #         fields = ['product', 'quantity']
#
#
# class OrderToGetSerializer(serializers.ModelSerializer):
#     products = serializers.SerializerMethodField()
#     # client_name = serializers.SerializerMethodField()
#     # total = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Order
#         # fields = ['id', 'client', 'client_name', 'created_at', 'modified_at', 'products', 'total']
#         fields = ['id', 'client', 'created_at', 'modified_at', 'products']
#
#     def get_products(self, obj):
#         return [product for product in obj.products.all().values(
#             'product__name',
#             'product__price',
#             'quantity')]
#
#     # def get_client_name(self, obj):
#     #     return obj.client.name
#     #
#     # def get_total(self, obj):
#     #     return obj.total
