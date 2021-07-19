from rest_framework import serializers
from clients.models import Order, Product, OrderProduct
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class OrderProductSerializer(WritableNestedModelSerializer, serializers.Serializer):
    # order = serializers.SerializerMethodField()
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    quantity = serializers.IntegerField()

    # def get_order(self):

    # class Meta:
    #     model = OrderProduct
    #     fields = ['id', 'product', 'quantity']
    #     # fields = '__all__'
    #
    #     depth = 1


class OrderSerializer(serializers.ModelSerializer):
# class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        # fields = [
        #     'id',
        #     'client',
        #     'created_at',
        #     'products'
        # ]
        fields = '__all__'
        depth = 0

    def create(self, validated_data):
        print('#-#'*155)
        # print(validated_data)
        # print()
        # print(dir(validated_data))

        order_products = validated_data.pop('products', None)
        order = super().create(validated_data)


        # print(validated_data)
        # print()
        # print(dir(validated_data))
        # print()
        # print(order_products)
        # print(order)
        # print()
        # print(dir(order_products))
        # print()

        for product in order_products:
            print(order_products)
            print(type(product))
            print(dir(product))
            print(dict(product))
            # print(**product)
            # product = Product.objects.get(id=product.get('id'))
            # print(product)
            # print(dir(product))
            print('#-#' * 155)

            OrderProduct.objects.get(order=order, **product)

        return order















