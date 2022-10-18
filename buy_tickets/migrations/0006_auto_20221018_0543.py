# Generated by Django 3.2.16 on 2022-10-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_images'),
        ('buy_tickets', '0005_rename_departures_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(through='buy_tickets.OrderItem', to='tickets.Ticket'),
        ),
    ]