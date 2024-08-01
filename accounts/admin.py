from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(UserAccount, UserAccountAdmin)