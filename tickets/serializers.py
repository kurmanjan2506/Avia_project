from django.db.models import Avg
from rest_framework import serializers
from .models import Ticket, Company, Favorites


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['rating_count'] = instance.reviews.count()
        return repr


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('from_city', 'to_city', 'date', 'price')


class TicketDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('company',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['companies'] = CompanySerializer(instance.companies).data
        return repr