from rest_framework import serializers
from .models import PaymentTier

class PaymentTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTier
        fields = ['id', 'customer_id', 'order_id', 'tier_one', 'tier_two', 'tier_three']
        depth = 1
    customer_id = serializers.IntegerField(write_only=True)
    order_id = serializers.IntegerField(write_only=True)