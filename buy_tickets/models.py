from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth import get_user_model

import tickets.models
from tickets.models import Ticket

User = get_user_model()


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(tickets.models.Ticket, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(tickets.models.Ticket, related_name='orders_product', null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    password_series = models.CharField(max_length=2, null=True)
    password_number = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField('email address', null=True)



    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.product}'