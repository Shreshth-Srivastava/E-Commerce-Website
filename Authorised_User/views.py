from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from App.models import Product, Customer, WishlistItem, Order, OrderItem
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib import messages
import json

# Create your views here.

def mylogin(request):
    customers = Customer.objects.all()
    if(request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        for customer in customers:
            if((username == customer.username) & (password == customer.password)):
                myuser = customer.user
                user = authenticate(username=myuser.username, password=password)
                if user is not None:
                    login(request, myuser)
                    return redirect('home2', myuser.id)
                else:
                    get_object_or_404(Customer, username = username)
            else:
                get_object_or_404(Customer, username = username)
    return render(request, 'login.html')

def mysignup(request):
    if request.method == "POST":
        # username = request.POST.get("username") --> First way
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]

        if User.objects.filter(username=username):
            messages.error(request,"Username already taken !")
            return redirect("signup")
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already registered !")
            return redirect("signup")

        if password != confirm:
            messages.error(request,"Entered passwords do not match !")
            return redirect("signup")

        if len(username)>20:
            messages.error(request,"Username must be under 20 characters !")
            return redirect("signup")

        # if not username.isalnum():
        #     messages.error(request,"Username is not alpha numeric !")
        #     return redirect("signup")

        myuser = User.objects.create_user(username,email,password)
        myorder = Order.objects.create(user=myuser,transaction_id=fname+str(myuser.id))
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.is_staff = True
        myuser.save()

        newcustomer = Customer.objects.create(user=myuser, username=username, password=password, first_name=fname, last_name=lname, order_num = myorder.id)
        newcustomer.save()
        # messages.success(request,"New user created, I have sent you a confirmation email, confirm your account to activate it")
        return redirect('login')
    
    return render(request,'signup.html')

def mylogout(request):
    logout(request)
    return redirect('home')

def index2(request, id):
    products = Product.objects.all()
    user = User.objects.get(pk=id)
    context = {
        'products' : products,
        'user' : user
    }
    return render(request, 'index.html', context)

def inc_count(request, id, pk):
    item = OrderItem.objects.get(pk=pk)
    user = User.objects.get(id=id)
    user_order = Order.objects.get(id=user.customer.order_num)
    item.quantity += 1
    # user_order.num_items += 1
    user_order = Order.objects.get(id=user.customer.order_num)
    # user_order.cart += item.price
    item.save()
    user.customer.save()
    return redirect('cart', user.id)

def dec_count(request, id, pk):
    item = OrderItem.objects.get(pk=pk)
    user = User.objects.get(id=id)
    item.quantity -= 1
    user_order = Order.objects.get(id=user.customer.order_num)
    # user_order.cart -= item.price
    # user_order.num_items -= 1
    item.save()
    user.customer.save()
    return redirect('cart', user.id)

def cartadd(request, userid, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=userid)
    user_order = Order.objects.get(id=user.customer.order_num)
    OrderItem.objects.create(order=user_order,product=product,quantity=1,price=product.price)
    # user_order.cart += product.price
    # user_order.num_items += 1
    user.customer.save()
    return redirect('details', user.id, product.id)

def cartremove(request, userid, itemid):
    item = OrderItem.objects.get(id=itemid)
    user = User.objects.get(id=userid)
    user_order = Order.objects.get(id=user.customer.order_num)
    # user_order.cart -= item.price
    # user_order.num_items -= 1
    user.customer.save()
    item.delete()
    return redirect('cart', userid)

def cartadd_wislist(request, userid, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=userid)
    user_order = Order.objects.get(id=user.customer.order_num)
    OrderItem.objects.create(order=user_order,product=product,quantity=1,price=product.price)
    # user_order.cart += product.price
    # user_order.num_items -= 1
    user.customer.save()
    return redirect('wishlist', user.id)

def AddToWishlist(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    WishlistItem.objects.create(user=user, name=product.name, price=product.price, img=product.img)
    return redirect('details', user.id, product.id)

def RemoveFromWishlist_Details(request, pk, id):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    item = WishlistItem.objects.filter(user=user, name=product.name)
    item.delete()
    return redirect('details', user.id, product.id)

def RemoveFromWishlist(request, id, pk):
    user = User.objects.get(id=id)
    wishlistitem = WishlistItem.objects.get(pk=pk)
    wishlistitem.delete()
    return redirect('wishlist', user.id)

def AddToWishlist_category(request, id, pk):
    product = Product.objects.get(pk=pk)
    user = User.objects.get(id=id)
    WishlistItem.objects.create(user=user, name=product.name, price=product.price, img=product.img)
    return redirect('category2', user.id, product.category)

def RemoveFromWishlist_category(request, pk, category):
    user = request.user
    wishlistitem = WishlistItem.objects.get(pk=pk)
    wishlistitem.delete()
    return redirect('category2', user.id, category)

def Wishlist(request, id):
    user = User.objects.get(id=id)
    wishlistitems = WishlistItem.objects.filter(user=user)
    context = {
        'products' : wishlistitems,
        'user' : user,
    }
    return render(request,'Auth/wishlist.html',context)

def Cart(request, id):
    # products = Product.objects.all()
    user = User.objects.get(id=id)
    user_order = Order.objects.get(id=user.customer.order_num)
    items = OrderItem.objects.filter(order=user_order)
    context = {
        'items' : items,
        'user' : user,
        'order' : user_order
    }
    return render(request,'Auth/cart.html',context)

def Checkout(request, userid):
    user = User.objects.get(id=userid)
    user_order = Order.objects.get(id=user.customer.order_num)
    items = OrderItem.objects.filter(order=user_order)
    context={
        'items':items,
        'user': user,
    }

    if(request.method == "POST"):
        payment = request.POST['payment']
        myorder = Order.objects.create(user=user)
        myorder.transaction_id = transaction_id=user.customer.first_name + str(myorder.id)
        user.customer.order_num = myorder.id
        user.customer.save()
        myorder.save()
        return redirect('placed', user.id)

    return render(request,'Auth/checkout.html',context)

def OrderPlaced(request,userid):
    user = User.objects.get(id=userid)
    context = {
        'user': user,
    }
    return render(request,'Auth/placed.html',context)

def Category(request, id ,category):
    user = User.objects.get(id=id)
    products = Product.objects.filter(category=category)
    wishlist = WishlistItem.objects.filter(user=user)
    # wishlist = WishlistItem.objects.filter(user=user).values_list('name') !!New!!
    context = {
        'products': products,
        'user': user,
        'wishlist': wishlist,
    }
    return render(request,'Auth/category.html',context)

def wishlist_json(request):
    data = list(WishlistItem.objects.filter(user=request.user).values())
    return JsonResponse(data, safe=False)

def product_json(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)

def Details(request, user_id, product_id):
    user = User.objects.get(id = user_id)
    product = Product.objects.get(id = product_id)
    user_wishlist = WishlistItem.objects.filter(user=user)
    user_order = Order.objects.get(id=user.customer.order_num)
    wishlist = user_wishlist.filter(name=product.name)
    user_cart = OrderItem.objects.filter(order=user_order)
    cart = user_cart.filter(product=product)
    context = {
        'user': user,
        'product': product,
        'wishlist': wishlist,
        'cart': cart
    }
    return render(request,'Auth/details.html',context)