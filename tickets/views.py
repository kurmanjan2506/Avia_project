from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Ticket
from . import serializers
from rest_framework.pagination import PageNumberPagination
from .service import TicketFilter


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 1000


class TicketViewSet(ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    queryset = Ticket.objects.all()
    filterset_class = TicketFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TicketListSerializer
        return serializers.TicketDetailSerializer




