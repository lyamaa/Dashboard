from django.contrib import admin
from django.urls import path, include
from django.urls import path

from .views import (
    PermissionAPIView,
    register,
    login,
    AuthenticationUser,
    logout,
    RoleViewSet
)

app_name = "accounts"

urlpatterns = [
    path("permissions", PermissionAPIView.as_view()),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("user", AuthenticationUser.as_view()),
    path("logout", logout, name="logout"),
    path('rples', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
