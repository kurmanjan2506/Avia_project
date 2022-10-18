# Generated by Django 3.2.16 on 2022-10-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_rename_tickets_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='`/images/'),
        ),
    ]