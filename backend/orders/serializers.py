from pyexpat import model
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'order_date']
        depth = 1
    user_id = serializers.IntegerField(write_only=True)