# serializers.py

from rest_framework import serializers
from erp.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Order
        fields = ['id', 'product', 'amount']