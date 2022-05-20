from django.db import models
from authentication.models import User
# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.IntegerField(max_length=255)
    member_since = models.DateField()
    money_owed = models.DecimalField(max_digits=9, decimal_places=2)

