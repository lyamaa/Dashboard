from django.contrib import admin
from django.urls import path, include
from django.urls import path

from .views import (
    PermissionAPIView,
    register,
    login,
    AuthenticationUser,
    logout,
    RoleViewSet,
    UserGenericApiView,
    ProfileInfoAPIView,
    ProfilePasswordApiView,
)

app_name = "accounts"

urlpatterns = [
    path("permissions", PermissionAPIView.as_view()),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("user", AuthenticationUser.as_view()),
    path("logout", logout, name="logout"),
    path("roles", RoleViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "roles/<str:pk>",
        RoleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
    ),
    path("user/info", ProfileInfoAPIView.as_view()),
    path("user/password", ProfilePasswordApiView.as_view()),
    path("users", UserGenericApiView.as_view()),
    path("user/<str:pk>", UserGenericApiView.as_view()),
]
