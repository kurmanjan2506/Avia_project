from django.contrib import admin
from rating.models import Review


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('owner', 'company', 'rating', 'created_at')
