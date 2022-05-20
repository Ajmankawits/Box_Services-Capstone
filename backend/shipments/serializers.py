from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'order_id', 'shipment_date']
        depth = 1
    order_id = serializers.IntegerField(write_only=True)
