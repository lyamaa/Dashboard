from django.db.models import Q
from rest_framework import (
    exceptions, 
    viewsets, 
    status, 
    generics, 
    mixins
    )
from rest_framework import views
from .permissions import PermissionsView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Role, User, Permission
from .authentication import generate_access_token, JWTauthentication
from .serializers import (
    UserSerializer, 
    PermissionSerializer, 
    RoleSerializers,
    ChangePassword
    )
from base.pagination import CustomPagination


@api_view(["GET"])
def users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register(request):
    data = request.data
    if data["password"] != data["password_confirm"]:
        raise exceptions.APIException("Password Do not Match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def login(request, *args, **kwargs):
    if request.user.is_authenticated:
        return Response({'Message': 'You are already logged in ...'}, status=400)
    username = request.data.get("username")
    password = request.data.get("password")

    user = (
        User.objects.filter(Q(username__iexact=username)
                            | Q(email__iexact=username))
        .distinct()
        .first()
    )

    if user is None:
        raise exceptions.AuthenticationFailed("user not found")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect password")

    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {"jwt": token}
    return response


@api_view(["POST"])
def logout(request):
    response = Response()
    response.delete_cookie(key="jwt")
    response.data = {"message": "success"}
    return response


class AuthenticationUser(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        data = UserSerializer(request.user).data
        data['permissions'] = [p['name'] for p in data['role']['permissions']]

        return Response({"data": data})


class PermissionAPIView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)

        return Response({
            'data': serializer.data
        })


""" Viewsets for role """
class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated & PermissionsView]
    permission_object = 'roles'


    def list(self, request):
        serializer = RoleSerializers(Role.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = RoleSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None,):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializers(role)

        return Response({
            "data": serializer.data
        })

    def update(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializers(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class UserGenericApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated & PermissionsView]
    permission_object = 'users'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })
        return self.list(request)
        
    
    def post(self, request):
        request.data.update({
            'password': 1234,
            'role': request.data['role_id']
        })
        return Response({
            'data': self.create(request).data
        })
    
    def put(self, request, pk=None):

        if request.data['role_id']:
            request.data.update({
                'role': request.data['role_id']
            })

        return Response({
            'data': self.partial_update(request, pk).data
        })

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ProfileInfoAPIView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ProfilePasswordApiView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):
        user = request.user

        if request.data['password'] != request.data['password_confirm']:
            raise exceptions.ValidationError('Password Do not Match')
        serializer = ChangePassword(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
