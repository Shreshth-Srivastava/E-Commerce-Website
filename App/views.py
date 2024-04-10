from django.shortcuts import render, redirect
from .models import Product, User

# Create your views here.
def index(request):
    products = Product.objects.all()
    user = User.objects.get(pk=1)
    context = {
        'products' : products,
        'user' : user
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
    return redirect('category',product.category)

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
    user = User.objects.get(pk=1)
    product.wishlist = True
    user.wishlist += 1
    product.save()
    user.save()
    return redirect('category',product.category)

def RemoveFromWishlist(request, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(pk=1)
    product.wishlist = False
    user.wishlist -= 1
    product.save()
    user.save()
    return redirect('wishlist')

def Wishlist(request):
    products = Product.objects.all()
    user = User.objects.get(pk=1)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request,'wishlist.html',context)

def Cart(request):
    products = Product.objects.all()
    user = User.objects.get(pk=1)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request,'cart.html',context)

def Checkout(request, pk):
    user = User.objects.get(pk=pk)
    context={
        'user': user,
    }
    return render(request,'checkout.html',context)

def Category(request, category):
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
    }
    return render(request,'category.html',context)
