from django.contrib import admin
from django.db.models import Count

from adminpage.admin import staffadmin_site
from .models import Classes, ClassName
from students.admin import StudentsInline

@admin.register(Classes, site=staffadmin_site)
class ClassesRegister(admin.ModelAdmin):
    inlines = [StudentsInline]
    readonly_fields = ("school",)
    list_display = ("name", "teacher_full_name", "teacher_telegram_id", "updated")
    search_fields = ("name__name", "teacher_full_name", "teacher_telegram_id")

@admin.register(ClassName, site=staffadmin_site)
class ClassNameRegister(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ClassesInline(admin.TabularInline):
    model = Classes
    extra = 0
    fields = ('name', )
    show_change_link = True