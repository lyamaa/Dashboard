from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from accounts.authentication import JWTauthentication
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from base.pagination import CustomPagination


class OrderGenericAPIView(
    generics.GenericAPIView, 
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin
    ):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': self.retrieve(request, pk).data
            })
        return self.list(request)