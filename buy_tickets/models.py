from django.db import models
from django.contrib.auth import get_user_model
from tickets.models import Ticket

User = get_user_model()
# STATUS_CHOICES = (
#     ('open', 'Открыт'),
#     ('in_process', 'В обработке'),
#     ('closed', 'Закрыт')
# )


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Ticket, related_name='orders', null=True, on_delete=models.CASCADE)
    arrivals = models.ForeignKey(Ticket, related_name='arrivals', null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.product} -> {self.date}'

