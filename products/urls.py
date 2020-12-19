
from django.urls import path, include

from .views import ProductGenericAPIView

app_name = 'products'

urlpatterns = [
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view())
    
]
