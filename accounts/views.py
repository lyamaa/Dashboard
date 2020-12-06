from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import User

from .serializers import UserSerializer

@api_view(['GET'])
def users(request):
    user = User.objects.all()
    return Response(user)

@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Password Do not Match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)