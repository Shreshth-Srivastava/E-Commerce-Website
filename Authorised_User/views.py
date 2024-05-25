from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from App.models import Product, Customer, WishlistItem

# Create your views here.

def login(request):
    customers = Customer.objects.all()
    if(request.method == "POST"):
        userID = request.POST["userID"]
        password = request.POST["password"]
        for customer in customers:
            if((userID == customer.userID) & (password == customer.password)):
                return redirect('home2', customer.user.pk)
            else:
                get_object_or_404(Customer, userID = userID)
    return render(request, 'login.html')

def index2(request, id):
    products = Product.objects.all()
    user = User.objects.get(pk=id)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request, 'Auth/index.html', context)

def inc_count(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = Customer.user.objects.get(id=id)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('cart', user.userID)

def dec_count(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = Customer.objects.get(userID=userID)
    product.value -= 1
    user.cart -= 1
    user.orderPrice -= product.price
    product.save()
    user.save()
    return redirect('cart', user.userID)

def cartadd(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = Customer.objects.get(userID=userID)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('category2', user.userID, product.category)

def cartadd_wislist(request, userID, pk):
    product = Product.objects.get(pk=pk)
    user = Customer.objects.get(userID=userID)
    product.value += 1
    user.cart += 1
    user.orderPrice += product.price
    product.save()
    user.save()
    return redirect('wishlist', user.userID)

def AddToWishlist(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    WishlistItem.objects.create(user=user, name=product.name, price=product.price, img=product.img)
    return redirect('category2', user.id, product.category)

def RemoveFromWishlist(request, id, pk):
    user = User.objects.get(id=id)
    wishlistitem = WishlistItem.objects.get(pk=pk)
    wishlistitem.delete()
    return redirect('wishlist', user.id)

'''def AddToWishlist(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    customer = user.customer
    product.wishlist = True
    customer.wishlist += 1
    product.save()
    customer.save()
    return redirect('category2', user.id, product.category)'''

'''def RemoveFromWishlist(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    customer = user.customer
    product.wishlist = False
    user.wishlist -= 1
    product.save()
    user.save()
    return redirect('wishlist', user.id)'''

def Wishlist(request, id):
    user = User.objects.get(id=id)
    wishlistitems = WishlistItem.objects.filter(user=user)
    context = {
        'products' : wishlistitems,
        'user' : user
    }
    return render(request,'Auth/wishlist.html',context)

def Cart(request, userID):
    products = Product.objects.all()
    user = Customer.objects.get(userID=userID)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request,'Auth/cart.html',context)

def Checkout(request, userID):
    user = Customer.objects.get(userID=userID)
    context={
        'user': user,
    }
    return render(request,'Auth/checkout.html',context)

def Category(request, id ,category):
    user = User.objects.get(id=id)
    products = Product.objects.filter(category=category)
    wishlist = WishlistItem.objects.filter(user=user)
    flag = False
    context = {
        'products': products,
        'user': user,
        'wishlist': wishlist,
        'flag': flag
    }
    return render(request,'Auth/category.html',context)
