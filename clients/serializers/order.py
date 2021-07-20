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


class OrderProductToGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderToGetSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    # clients = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    # def get_clients(self, obj):
    #     print(obj)
    #     print()
    #     print(obj.__dict__)
    #     print()
    #     print(dir(obj))
    #     return 'Hello world'

    def get_products(self, obj):
        return [product for product in obj.products.all().values(
            'product__name',
            'product__price',
            'quantity',
        )]



