from django.shortcuts import render, redirect, get_object_or_404
from App.models import Product, User
# Create your views here.

def login(request):
    users = User.objects.all()
    if(request.method == "POST"):
        userID = request.POST["userID"]
        password = request.POST["password"]
        for user in users:
            if((userID == user.userID) & (password == user.password)):
                return redirect('home2', userID)
            else:
                get_object_or_404(User, userID = userID)
    return render(request, 'login.html')

def index2(request, userID):
    products = Product.objects.all()
    user = User.objects.get(userID = userID)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request, 'Auth/index.html', context)

def inc_count(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('cart', user.userID)

def dec_count(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.value -= 1
    user.cart -= 1
    user.orderPrice -= product.price
    product.save()
    user.save()
    return redirect('cart', user.userID)

def cartadd(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('category2', user.userID, product.category)

def cartadd_wislist(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('wishlist', user.userID)

def AddToWishlist(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.wishlist = True
    user.wishlist += 1
    product.save()
    user.save()
    return redirect('category2', user.userID, product.category)

def RemoveFromWishlist(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(userID=userID)
    product.wishlist = False
    user.wishlist -= 1
    product.save()
    user.save()
    return redirect('wishlist', userID)

def Wishlist(request,userID):
    products = Product.objects.all()
    user = User.objects.get(userID=userID)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request,'Auth/wishlist.html',context)

def Cart(request, userID):
    products = Product.objects.all()
    user = User.objects.get(userID=userID)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request,'Auth/cart.html',context)

def Checkout(request, userID):
    user = User.objects.get(userID=userID)
    context={
        'user': user,
    }
    return render(request,'Auth/checkout.html',context)

def Category(request, userID ,category):
    user = User.objects.get(userID=userID)
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'user': user
    }
    return render(request,'Auth/category.html',context)
