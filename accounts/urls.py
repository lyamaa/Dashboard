from django.contrib import admin
from django.urls import path, include
from .views import users, register, login

app_name = "accounts"

urlpatterns = [
   path("users", users, name="hello_daju" ),
   path("register", register, name="register"),
   path('login', login, name="login")
   
]
