from django.contrib import admin
from adminpage.admin import staffadmin_site
from .models import Students

class StudentsInline(admin.TabularInline):
    model = Students
    extra = 0
    fields = ('full_name', )
    show_change_link = True

@admin.register(Students, site=staffadmin_site)
class StudentsRegister(admin.ModelAdmin):
    list_display = ['full_name', 'status', '_class']
    search_fields = ['full_name', 'status']
