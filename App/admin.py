from django.contrib import admin
from django.contrib.auth.models import User
from .models import Product, Customer, WishlistItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(WishlistItem)