from django.contrib import admin
from .models import School

@admin.register(School)
class SchoolRegister(admin.ModelAdmin):
    list_display = ['name', 'admin']
    search_fields = ['name', 'admin']
