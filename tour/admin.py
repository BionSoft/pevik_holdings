from django.contrib import admin
from .models import Tour

class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'available_day')

admin.site.register(Tour, TourAdmin)