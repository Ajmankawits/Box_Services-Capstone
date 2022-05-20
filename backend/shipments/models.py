from django.db import models
from orders.models import Order
# Create your models here.

class Shipment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_date = models.DateField()