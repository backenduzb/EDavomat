from django.contrib import admin
from adminpage.admin import staffadmin_site
from .models import Students

@admin.register(Students, site=staffadmin_site)
class StudentsRegister(admin.ModelAdmin):
    list_display = ['full_name', 'status']
    search_fields = ['full_name', 'status']
    