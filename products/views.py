from django.core.files.storage import default_storage
from django.conf import settings
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.authentication import JWTauthentication

from products.models import Product
from products.serializers import ProductSerializer
from base.pagination import CustomPagination

from PIL import Image
import cloudinary
import cloudinary.uploader
import json


class ProductGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})
        return self.list(request)

    def post(self, request):

        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class FileUploadView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def post(self, request):

        file = request.data.get("image")

        upload_data = cloudinary.uploader.upload(file)
        url = upload_data.get("secure_url")

        # url = default_storage.url(file_name)

        return Response(
            {
                "status": "success",
                "url": url,
            }
        )
