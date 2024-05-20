from rest_framework import serializers
from .models import Product, ProductOption

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['month_6', 'month_12', 'month_24', 'month_36']

class ProductSerializer(serializers.ModelSerializer):
    product_option = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'product_option']