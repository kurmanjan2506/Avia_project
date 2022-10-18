from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth import get_user_model

import tickets.models
from tickets.models import Ticket

User = get_user_model()
# STATUS_CHOICES = (
#     ('open', 'Открыт'),
#     ('in_process', 'В обработке'),
#     ('closed', 'Закрыт')
# )


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(tickets.models.Ticket, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    # user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(tickets.models.Ticket, related_name='orders', null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    password_series = models.CharField(max_length=2, null=True)
    password_number = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField('email address', unique=True, null=True)

# class UserManager(BaseUserManager):
#      use_in_migrations = True
#
#      def _create_user(self, email, password, **kwargs):
#         if not email:
#              return ValueError('The given email must be set!')
#         email = self.normalize_email(email=email)
#         user = self.model(email=email, **kwargs)
#         user.create_activation_code()
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **kwargs):
#         kwargs.setdefault('is_staff', False)
#         kwargs.setdefault('is_superuser', False)
#         return self._create_user(email, password, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.product}'