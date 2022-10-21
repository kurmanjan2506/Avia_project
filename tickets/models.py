from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.title


class Ticket(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companies')
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    count_of_product = models.SmallIntegerField(blank=True, null=True)
    images = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return f'{self.from_city} -> {self.to_city}\n{self.price}\n{self.date}->{self.time} '

