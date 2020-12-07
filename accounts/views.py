from django.shortcuts import render
from django.db.models import Q
from rest_framework import exceptions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import User
from .authentication import generate_access_token, JWTauthentication
from .serializers import UserSerializer

@api_view(['GET'])
def users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Password Do not Match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def login(request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct().first()


    if user is None:
        raise exceptions.AuthenticationFailed("user not found")
    
    if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect password")
    
    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'success'
    }
    return response


class AuthenticationUser(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        serializer = UserSerializer(request.user)
        
        return Response({
            'data': serializer.data
        })


