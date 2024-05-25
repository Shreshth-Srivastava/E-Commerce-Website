from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    # value = models.IntegerField(default=1)
    name = models.CharField(default = "Product",max_length=200)
    category = models.CharField(default = 'not defined', max_length = 50)
    img = models.CharField(default = "#",max_length=200)
    price = models.IntegerField(default = 0)
    value = models.IntegerField(default   = 0)
    # wishlist = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    userID = models.CharField(default = None, null = True, blank = True, max_length=10)
    username = models.CharField(default = "User",null = False, max_length = 200)
    password = models.CharField(default = None, null = True, max_length=15)
    cart = models.IntegerField(default = 0)
    orderPrice = models.IntegerField(default = 0)
    # wishlist = models.IntegerField(default = 0)

    def __str__(self):
        return self.username
    
'''class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)
'''
    
class WishlistItem(models.Model):
    # wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    price = models.IntegerField(default=0)
    img = models.CharField(default = "#",max_length=200)

    def __str__(self):
        return self.name
    