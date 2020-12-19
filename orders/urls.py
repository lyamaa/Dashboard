from django.urls import path

from .views import OrderGenericAPIView

app_name = "orders"

urlpatterns = [
    path("orders", OrderGenericAPIView.as_view()),
    path("orders/<str:pk>", OrderGenericAPIView.as_view()),
]
