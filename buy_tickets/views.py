from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions

from tickets.models import Ticket
from .models import Order
from .serializers import OrderSerializer


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer

    # def post(self, request, *args, **kwargs):
    #     buy = Order.objects.all()
    #
    #     return self.create(request, *args, **kwargs)



class UserOrderList(APIView):
    def get(self, request):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)
