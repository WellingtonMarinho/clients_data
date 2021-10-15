from rest_framework import serializers
from clients.models import Product


class ProductSerializer(serializers.ModelSerializer):
    absolute_url_api = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'absolute_url_api']

    def get_absolute_url_api(self, obj):
        return obj.absolute_url_api()


class ProductDetailSerializer(serializers.ModelSerializer):
    absolute_url_api = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

    def get_absolute_url_api(self, obj):
        return obj.absolute_url_api()
