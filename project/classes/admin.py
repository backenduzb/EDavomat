from django.db.models import Count
from django.contrib import admin
from adminpage.admin import (
    staffadmin_site
)
from .models import (
    Classes, ClassName,
    Statistics
)

@admin.register(Statistics, site=staffadmin_site)
class StatisticsRegister(admin.ModelAdmin):
    list_display = ("created_at", "_class", "reason_students_count", "no_reason_students_count")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            reason_cnt=Count("reason_students", distinct=True),
            noreason_cnt=Count("no_reason_students", distinct=True),
        )

    @admin.display(description="Sababli (count)")
    def reason_students_count(self, obj):
        return obj.reason_cnt

    @admin.display(description="Sababsiz (count)")
    def no_reason_students_count(self, obj):
        return obj.noreason_cnt

@admin.register(Classes, site=staffadmin_site)
class ClassesRegister(admin.ModelAdmin):
    list_display = ['name', 'teacher_full_name', 'teacher_telegram_id', 'updated']
    search_fields = ['name', 'teacher_full_name', 'teacher_telegam_id']
        
@admin.register(ClassName, site=staffadmin_site)
class ClassNameRegister(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
