from django.db import models
from customers.models import Customer
# Create your models here.

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()