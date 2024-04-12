from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:userID>', views.index2, name="home2")
]
