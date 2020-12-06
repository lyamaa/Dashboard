from django.contrib import admin
from django.urls import path, include
from .views import hello_daju

app_name = "accounts"

urlpatterns = [
   path("hello", hello_daju, name="hello_daju" )
   
]
