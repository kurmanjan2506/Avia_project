from django.db import models
from tickets.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    marks = ((one, 'Ужасно'), (two, 'Плохо'), (three, 'Нормально'), (four, 'Хорошо'), (five, 'Отлично!'))


class Review(models.Model):
    # company = models.ForeignKey(, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)


