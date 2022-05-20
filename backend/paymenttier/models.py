from django.db import models
from authentication.models import User
from orders.models import Order
# Create your models here.

class PaymentTier(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    tier_one = models.CharField(max_length=255)
    tier_two = models.CharField(max_length=255)
    tier_three = models.CharField(max_length=255)