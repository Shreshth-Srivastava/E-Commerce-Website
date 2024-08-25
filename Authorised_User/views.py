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
                    return redirect('home2')
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

        newcustomer = Customer.objects.create(user=myuser, username=username, password=password, first_name=fname, last_name=lname)
        newcustomer.save()
        # messages.success(request,"New user created, I have sent you a confirmation email, confirm your account to activate it")
        return redirect('login')
    
    return render(request,'signup.html')

def mylogout(request):
    logout(request)
    return redirect('home')

def index2(request):
    products = Product.objects.all()
    user = request.user
    context = {
        'products' : products,
        'user' : user
    }
    return render(request, 'index.html', context)

def inc_count(request, pk):
    item = OrderItem.objects.get(pk=pk)
    user = request.user
    # user_order = Order.objects.get(user=user, placed=False)
    item.quantity += 1
    # user_order.num_items += 1
    # user_order.cart += item.price
    item.save()
    user.customer.save()
    return redirect('cart')

def dec_count(request, pk):
    item = OrderItem.objects.get(pk=pk)
    user = request.user
    item.quantity -= 1
    # user_order = Order.objects.get(user=user, placed=False)
    # user_order.cart -= item.price
    # user_order.num_items -= 1
    item.save()
    user.customer.save()
    return redirect('cart')

def cartadd(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    user_order = Order.objects.get(user=user, placed=False)
    OrderItem.objects.create(order=user_order,product=product,quantity=1,price=product.price)
    # user_order.cart += product.price
    # user_order.num_items += 1
    user.customer.save()
    return redirect('details',product.id)

def cartremove(request, itemid):
    item = OrderItem.objects.get(id=itemid)
    user = request.user
    # user_order = Order.objects.get(user=user, placed=False)
    # user_order.cart -= item.price
    # user_order.num_items -= 1
    user.customer.save()
    item.delete()
    return redirect('cart')

def cartadd_wislist(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    user_order = Order.objects.get(user=user, placed=False)
    OrderItem.objects.create(order=user_order,product=product,quantity=1,price=product.price)
    # user_order.cart += product.price
    # user_order.num_items -= 1
    user.customer.save()
    return redirect('wishlist',)

def AddToWishlist(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    WishlistItem.objects.create(user=user, name=product.name, price=product.price, img=product.img.url)
    return redirect('details', product.id)

def RemoveFromWishlist_Details(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    item = WishlistItem.objects.filter(user=user, name=product.name)
    item.delete()
    return redirect('details', product.id)

def RemoveFromWishlist(request, pk):
    user = request.user
    wishlistitem = WishlistItem.objects.get(pk=pk)
    wishlistitem.delete()
    return redirect('wishlist')

def AddToWishlist_category(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    WishlistItem.objects.create(user=user, name=product.name, price=product.price, img=product.img.url)
    return redirect('category', product.category)

def RemoveFromWishlist_category(request, pk, category):
    user = request.user
    wishlistitem = WishlistItem.objects.get(pk=pk)
    wishlistitem.delete()
    return redirect('category', category)

def Wishlist(request):
    user = request.user
    wishlistitems = WishlistItem.objects.filter(user=user)
    context = {
        'products' : wishlistitems,
        'user' : user,
    }
    return render(request,'Auth/wishlist.html',context)

def Cart(request):
    # products = Product.objects.all()
    user = request.user
    user_order = Order.objects.get(user=user, placed=False)
    items = OrderItem.objects.filter(order=user_order)
    context = {
        'items' : items,
        'user' : user,
        'order' : user_order
    }
    return render(request,'Auth/cart.html',context)

def Checkout(request):
    user = request.user
    user_order = Order.objects.get(user=user, placed=False)
    items = OrderItem.objects.filter(order=user_order)
    context={
        'items':items,
        'order': user_order,
        'user': user,
    }

    if(request.method == "POST"):
        payment = request.POST['payment']
        old_order = Order.objects.get(user=user, placed=False)
        old_order.placed = True
        old_order.payment = payment
        myorder = Order.objects.create(user=user)
        myorder.transaction_id = user.customer.first_name + str(myorder.id)
        # user.customer.order_num = myorder.id
        user.customer.save()
        myorder.save()
        old_order.save()
        return redirect('placed')

    return render(request,'Auth/checkout.html',context)

def OrderPlaced(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request,'Auth/placed.html',context)

def Category(request, category):
    products = Product.objects.filter(category=category)
    if request.user.is_authenticated:
        user = request.user
        wishlist = WishlistItem.objects.filter(user=user)
        # wishlist = WishlistItem.objects.filter(user=user).values_list('name') !!New!!
    else:
        user = {}
        wishlist = {}
    context = {
        'products': products,
        'user': user,
        'wishlist': wishlist,
    }
    return render(request,'category.html',context)

def Details(request, product_id):
    user = request.user
    product = Product.objects.get(id = product_id)
    user_wishlist = WishlistItem.objects.filter(user=user)
    user_order = Order.objects.get(user=user, placed=False)
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

def Orders(request):
    user = request.user
    all_orders = Order.objects.filter(user=user, placed=True)
    orders = all_orders.order_by("-date_ordered")
    context={
        'user': user,
        'orders': orders,
    }
    return render(request,'Auth/orders.html',context)

def Order_Details(request, orderid):
    user = request.user
    items = OrderItem.objects.filter(order=orderid)
    # print(orderid)
    context = {
        'items': items,
        'user': user
    }
    return render(request, 'Auth/order_details.html',context)

def orders_json(request):
    data = list(Order.objects.filter(user=request.user).values())
    return JsonResponse(data, safe=False)

def wishlist_json(request):
    data = list(WishlistItem.objects.filter(user=request.user).values())
    return JsonResponse(data, safe=False)

def product_json(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)