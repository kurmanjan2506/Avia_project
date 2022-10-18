from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class Tickets(admin.ModelAdmin):
    list_display = ('company', 'from_city', 'to_city')
