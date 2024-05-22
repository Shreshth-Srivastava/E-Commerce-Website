from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('<str:userID>/', views.index2, name="home2"),
    path('cartadd/<str:userID>/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartadd_wishlist/<str:userID>/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('increase/<str:userID>/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<str:userID>/<int:pk>/', views.dec_count, name='decrease'),
    path('addtowishlist/<str:userID>/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('removefromwishlist/<str:userID>/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('wishlist/<str:userID>/', views.Wishlist, name='wishlist'),
    path('cart/<str:userID>/', views.Cart, name='cart'),
    path('checkout/<str:userID>/', views.Checkout, name='checkout'),
    path('category/<str:userID>/<str:category>/', views.Category, name='category2'),
]
