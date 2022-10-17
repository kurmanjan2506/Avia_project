from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import Tickets
from . import serializers


class TicketViewSet(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = serializers.TicketSerializers

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return (permissions.AllowAny(),)
        else:
            return (permissions.IsAdminUser(),)