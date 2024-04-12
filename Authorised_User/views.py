from django.shortcuts import render, redirect
from App.models import Product, User
# Create your views here.

def index2(request, userID):
    products = Product.objects.all()
    user = User.objects.get(userID = userID)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request, 'index.html', context)