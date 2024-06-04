from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.mylogin, name='login'),
    path('signup/', views.mysignup, name='signup'),
    path('logout/', views.mylogout, name='logout'),
    path('<int:id>/', views.index2, name="home2"),
    path('cartadd/<int:userid>/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartremove/<int:userid>/<int:itemid>/', views.cartremove, name='removefromcart'),
    path('cartadd_wishlist/<int:userid>/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('increase/<int:id>/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<int:id>/<int:pk>/', views.dec_count, name='decrease'),
    path('addtowishlist/<int:id>/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('addtowishlist_category/<int:id>/<int:pk>/', views.AddToWishlist_category, name='addtowishlist_category'),
    path('removefromwishlist/<int:id>/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('removefromwishlist_category/<int:pk>/<str:category>/', views.RemoveFromWishlist_category, name='removefromwishlist_category'),
    path('wishlist/<int:id>/', views.Wishlist, name='wishlist'),
    path('cart/<int:id>/', views.Cart, name='cart'),
    path('checkout/<int:id>/', views.Checkout, name='checkout'),
    path('category/<int:id>/<str:category>/', views.Category, name='category2'),
    path('category/<int:user_id>/<int:product_id>', views.Details, name='details'),
    path('wishlist/json/', views.wishlist_json, name='wishlistJSON'),
    path('product/json/', views.product_json, name='productJSON'),
]
