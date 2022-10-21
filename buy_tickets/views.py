from decouple import config
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from tickets.models import Ticket
from .models import Order
from .serializers import OrderSerializer

import smtplib


class CreateOrderView(CreateAPIView):
    queryset = Order.objects.all()
    # print('!!!!!!!!!!!!!!', queryset)
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)



class UserOrderList(APIView):
    def get(self, request):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)


#
@api_view(['POST'])
def send_email(request):
    sender = 'usermaks47@gmail.com'
    password = config('EMAIL_PASSWORD')
    serializer = OrderSerializer(data=request.POST)
    model_of_tickets = Ticket.objects.all()
    for model_of_ticket in model_of_tickets:
        print(model_of_ticket, '!!!!!')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # try:
    server.login(sender, password)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        server.sendmail(sender, serializer.data['email'], msg=f"{model_of_ticket}")
        return Response('The message was sent successfully')

def main():
    message = Ticket.objects.all()
    # message = input("text: ")
    return send_email(message=message)

if __name__ == '__main__':
    main()
