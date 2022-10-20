from django.db import models

import tickets.models
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
    company = models.ForeignKey(tickets.models.Company, on_delete=models.CASCADE, related_name='reviews', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    movie = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ['owner', 'movie']


