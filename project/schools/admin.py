from django.contrib import admin
from .models import School
from classes.admin import ClassesInline

@admin.register(School)
class SchoolRegister(admin.ModelAdmin):
    inlines = [ClassesInline]
    list_display = ['name', 'admin']
    search_fields = ['name', 'admin']
