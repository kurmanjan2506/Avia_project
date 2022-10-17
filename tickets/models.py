from django.db import models


class Company:
    tezjet = 'TEZ JET'
    air_kyrgyzstan = 'Air Kyrgyzstan'
    avia_traffic = 'Avia Traffic Company'
    companies = ((tezjet,'TEZ JET'), (air_kyrgyzstan,'Air Kyrgyzstan'), (avia_traffic,'Avia Traffic Company'))


class Tickets(models.Model):
    company = models.CharField(choices=Company.companies, max_length=100)
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    count_of_product = models.SmallIntegerField(blank=True, null=True)
    images = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return f'{self.from_city} -> {self.to_city}'

