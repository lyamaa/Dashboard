from django.urls import path

from .views import ProductGenericAPIView, FileUploadView

app_name = 'products'

urlpatterns = [
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('upload', FileUploadView.as_view())
    
] 

