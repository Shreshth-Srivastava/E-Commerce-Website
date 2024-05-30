from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('<int:id>/', views.index2, name="home2"),
    path('cartadd/<str:userID>/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartremove/<int:userid>/<int:itemid>/', views.cartremove, name='removefromcart'),
    path('cartadd_wishlist/<int:id>/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('increase/<int:id>/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<int:id>/<int:pk>/', views.dec_count, name='decrease'),
    path('addtowishlist/<int:id>/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('removefromwishlist/<int:id>/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('wishlist/<int:id>/', views.Wishlist, name='wishlist'),
    path('cart/<int:id>/', views.Cart, name='cart'),
    path('checkout/<int:id>/', views.Checkout, name='checkout'),
    path('category/<int:id>/<str:category>/', views.Category, name='category2'),
    path('category/<int:user_id>/<int:product_id>', views.Details, name='details'),
]


'''path('<str:userID>/', views.index2, name="home2"),
    path('cartadd/<str:userID>/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartadd_wishlist/<str:userID>/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('increase/<str:userID>/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<str:userID>/<int:pk>/', views.dec_count, name='decrease'),
    path('addtowishlist/<str:userID>/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('removefromwishlist/<str:userID>/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('wishlist/<str:userID>/', views.Wishlist, name='wishlist'),
    path('cart/<str:userID>/', views.Cart, name='cart'),
    path('checkout/<str:userID>/', views.Checkout, name='checkout'),
    path('category/<str:userID>/<str:category>/', views.Category, name='category2'),'''