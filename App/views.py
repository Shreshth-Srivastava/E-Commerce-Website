from django.shortcuts import render, redirect
from .models import Product, User

# Create your views here.
def index(request):
    products = Product.objects.all()
    users = User.objects.all()
    context = {
        'products' : products,
        'users' : users
    }
    return render(request, 'index.html', context)

def inc_count(request, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(pk=1)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('cart')

def dec_count(request, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(pk=1)
    product.value -= 1
    user.cart -= 1
    user.orderPrice -= product.price
    product.save()
    user.save()
    return redirect('cart')

def cartadd(request, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(pk=1)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('home')

def cartadd_wislist(request, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(pk=1)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('wishlist')

def AddToWishlist(request, pk):
    product = Product.objects.get(pk=pk)
    product.wishlist = True
    product.save()
    return redirect('home')

def RemoveFromWishlist(request, pk):
    product = Product.objects.get(pk=pk)
    product.wishlist = False
    product.save()
    return redirect('wishlist')

def Wishlist(request):
    products = Product.objects.all()
    return render(request,'wishlist.html',{"products": products})

def Cart(request):
    products = Product.objects.all()
    users = User.objects.all()
    context = {
        'products' : products,
        'users' : users
    }
    return render(request,'cart.html',context)