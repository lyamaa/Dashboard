from django.urls import path
from .views import (
   users, 
   register, 
   login, 
   AuthenticationUser, 
   logout
   )

app_name = "accounts"

urlpatterns = [
   path("users", users, name="hello_daju" ),
   path("register", register, name="register"),
   path('login', login, name="login"),
   path("user", AuthenticationUser.as_view()),
   path('logout', logout, name='logout')
   
]
