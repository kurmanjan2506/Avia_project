from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Order, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = OrderItem
        fields = ('product', 'product_title', 'quantity')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr.pop('product')
        return repr


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SendEmailSerializer(serializers.Serializer):
    email = serializers.CharField()
    message = serializers.ReadOnlyField()


    def validate(self, attrs):
        email = get_object_or_404(User, email=attrs.get('email'))
        message = get_object_or_404(Order, first_name=['message'], last_name=['message'])
        return attrs

