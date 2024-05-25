from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<str:category>/', views.Category, name='category1'),
]
