# Generated by Django 3.2.16 on 2022-10-18 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_tickets', '0004_auto_20221018_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='departures',
            new_name='product',
        ),
    ]
