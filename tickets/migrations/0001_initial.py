# Generated by Django 3.2.16 on 2022-10-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(choices=[('TEZ JET', 'TEZ JET'), ('Air Kyrgyzstan', 'Air Kyrgyzstan'), ('Avia Traffic Company', 'Avia Traffic Company')], max_length=100)),
                ('from_city', models.CharField(max_length=100)),
                ('to_city', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('count_of_product', models.SmallIntegerField(blank=True, null=True)),
                ('images', models.ImageField(upload_to='media/images/')),
            ],
        ),
    ]