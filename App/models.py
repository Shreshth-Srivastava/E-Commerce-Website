from django.db import models


# Create your models here.
class Product(models.Model):
    # value = models.IntegerField(default=1)
    img = models.CharField(default="#",max_length=200)
    price = models.IntegerField(default=0)
    name = models.CharField(default="Product",max_length=200)
    value = models.IntegerField(default = 0)
    wishlist = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(default = "User",null = False, max_length = 200)
    cart = models.IntegerField(default = 0)
    orderPrice = models.IntegerField(default = 0)