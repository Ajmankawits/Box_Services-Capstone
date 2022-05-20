from pyexpat import model
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'order_date']
        depth = 1
    customer_id = serializers.IntegerField(write_only=True)