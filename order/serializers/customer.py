from rest_framework import serializers
from order.models import Order
from clients.models import People



class CustomerOrdersSerialiazer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = People

    def get_orders(self, obj):
        print('###################' *8)
        print(obj)
        print(dir(obj))
        print(obj.__dict__)
        print()
        print()
        return 'AQUI'