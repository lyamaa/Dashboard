import csv
from django.db import connection
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.views import APIView
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


class ExportApiView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment: filename=orders.csv'
        orders = Order.objects.all()
        writer = csv.writer(response)
        writer.writerow(
            ['ID', 'Name', 'Email', 'Product Title', 'Price', 'Quantity'])

        for order in orders:
            writer.writerow([order.id, order.name, order.email, '', '', ])

        orderItems = OrderItem.objects.all().filter(order_id=order.id)

        for item in orderItems:
            writer.writerow(["", "", "", item.product_title,
                             item.price, item.quantity])

        return response


class ChartApiView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        with connection.cursor() as cursor:
            cursor.execute(""" 
            SELECT to_date(o.created_at::text, 'YYYY-MM-DD') as date, sum(i.quantity * i.price) as sum 
            From orders_order as o 
            JOIN orders_orderitem as i ON o.id = i.order_id
            GROUP BY date
            """)
            row = cursor.fetchall()
            data = [{
                'date': result[0],
                'sum': result[1]
            }for result in row]

            
            return Response({
                'data': data
            })
