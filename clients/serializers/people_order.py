from rest_framework import serializers
from clients.models import People
from order.serializers import OrderSerializer



class PeopleOrderSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    #
    # def get_orders(self, obj):
    #     return obj.orders.all()

    class Meta:
        model = People
        fields = ['name', 'cpf', 'slug', 'birth_date', 'sex', 'sign', 'orders']
