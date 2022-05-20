from django.db import models
from authentication.models import User
from datetime import date
# Create your models here.

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(default= date.today())