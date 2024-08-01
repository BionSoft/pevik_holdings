from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'project_type','featured')
    list_display_links = ('id', 'title')
    list_filter = ('project_type', )
    list_editable = ('is_published', 'featured')
    search_fields = ('title', 'description', 'address', 'price', 'project_type')
    list_per_page = 25

admin.site.register(Project, ProjectAdmin)