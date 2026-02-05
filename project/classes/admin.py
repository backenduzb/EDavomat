from django.contrib import admin
from django.db.models import Count

from adminpage.admin import staffadmin_site
from .models import Classes, ClassName
from students.admin import StudentsInline
from adminpage.filters import get_staff_school
from schools.models import School

@admin.register(Classes, site=staffadmin_site)
class ClassesRegister(admin.ModelAdmin):
    inlines = [StudentsInline]
    readonly_fields = ("school",)
    list_display = ("name", "teacher_full_name", "teacher_telegram_id", "updated")
    search_fields = ("name__name", "teacher_full_name", "teacher_telegram_id")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
    
        if request.user.is_superuser:
            return qs
    
        school = School.objects.filter(admin=request.user).first()
        if school:
            return qs.filter(school=school)
    
        return qs.none()


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "_class" and not request.user.is_superuser:
            school = get_staff_school(request)
            kwargs["queryset"] = Classes.objects.filter(school=school) if school else Classes.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
@admin.register(ClassName, site=staffadmin_site)
class ClassNameRegister(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ClassesInline(admin.TabularInline):
    model = Classes
    extra = 0
    fields = ('name', )
    show_change_link = True
