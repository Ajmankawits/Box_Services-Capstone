from django.db import models
from customers.models import Customer
from orders.models import Order
# Create your models here.

class PaymentTier(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    tier_one = models.CharField(max_length=255)
    tier_two = models.CharField(max_length=255)
    tier_three = models.CharField(max_length=255)