from django.contrib import admin
from adminpage.admin import (
    staffadmin_site
)
from .models import Classes, ClassName 


@admin.register(Classes, site=staffadmin_site)
class ClassesRegister(admin.ModelAdmin):
    list_display = ['name', 'teacher_full_name', 'teacher_telegram_id', 'updated']
    search_fields = ['name', 'teacher_full_name', 'teacher_telegam_id']
        
@admin.register(ClassName, site=staffadmin_site)
class ClassNameRegister(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
