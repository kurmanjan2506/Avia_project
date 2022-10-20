from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from .models import Ticket, Company
from . import serializers
from rest_framework.pagination import PageNumberPagination
from .service import TicketFilter
from rest_framework.decorators import action


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    max_page_size = 1000


class CompanyViewSet(ModelViewSet):
    serializer_class = serializers.CompanySerializer
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    queryset = Company.objects.all()
    search_fields = ['title']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    # api/v1/ticket/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        ticket = self.get_object()
        if request.method == 'GET':
            reviews = ticket.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if ticket.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв!', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, company=ticket)
        return response.Response(serializer.data, status=201)


class TicketViewSet(ModelViewSet):
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    queryset = Ticket.objects.all()
    filterset_class = TicketFilter
    search_fields = ['price']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.TicketListSerializer
        return serializers.TicketDetailSerializer









