from django.shortcuts import render, redirect
from .models import Product, Customer

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'index.html', context)

def Category(request, category):
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
    }
    return render(request,'category.html',context)
