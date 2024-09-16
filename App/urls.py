# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
# ]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.mylogin, name='login'),
    path('signup/', views.mysignup, name='signup'),
    path('logout/', views.mylogout, name='logout'),
    path('', views.index, name="home"),
    path('increase/<int:pk>/', views.inc_count, name='increase'),
    path('decrease/<int:pk>/', views.dec_count, name='decrease'),
    path('cartadd/<int:pk>/', views.cartadd, name='addtocart'),
    path('cartremove/<int:itemid>/', views.cartremove, name='removefromcart'),
    path('cartadd_wishlist/<int:pk>/', views.cartadd_wislist, name='addtocart_wishlist'),
    path('addtowishlist/<int:pk>/', views.AddToWishlist, name='addtowishlist'),
    path('addtowishlist_category/<int:pk>/', views.AddToWishlist_category, name='addtowishlist_category'),
    path('removefromwishlist/<int:pk>/', views.RemoveFromWishlist, name='removefromwishlist'),
    path('removefromwishlist_category/<int:pk>/<str:category>/', views.RemoveFromWishlist_category, name='removefromwishlist_category'),
    path('removefromwishlist_details/<int:pk>/', views.RemoveFromWishlist_Details, name='removefromwishlist_details'),
    path('wishlist/', views.Wishlist, name='wishlist'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('category/<str:category>/', views.Category, name='category'),
    path('category/<int:product_id>', views.Details, name='details'),
    path('placed/', views.OrderPlaced, name='placed'),
    path('orders/', views.Orders, name='orders'),
    path('order_details/<int:orderid>/', views.Order_Details, name='order_details'),
    path('wishlist/json/', views.wishlist_json, name='wishlistJSON'),
    path('product/json/', views.product_json, name='productJSON'),
    path('orders/json/', views.orders_json, name='ordersJSON'),
]
