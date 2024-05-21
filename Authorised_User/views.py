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
    return render(request, 'index.html', context)