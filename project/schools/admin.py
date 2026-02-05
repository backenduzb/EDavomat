from django.contrib import admin
from .models import School
from classes.admin import ClassesInline
from adminpage.filters import get_staff_school

@admin.register(School)
class SchoolRegister(admin.ModelAdmin):
    inlines = [ClassesInline]
    list_display = ['name', 'admin']
    search_fields = ['name', 'admin']
    