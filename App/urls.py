from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:userID>', views.index, name='home'),
    path('cartadd/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartadd_wishlist/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('increase/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<int:pk>/', views.dec_count, name='decrease'),
    path('addtowishlist/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('removefromwishlist/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('wishlist/', views.Wishlist, name='wishlist'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/<int:pk>/', views.Checkout, name='checkout'),
    path('category/<str:category>/', views.Category, name='category'),
]
