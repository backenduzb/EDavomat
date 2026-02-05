from django.contrib import admin
from adminpage.admin import staffadmin_site
from .models import Students
from schools.models import School

class StudentsInline(admin.TabularInline):
    model = Students
    extra = 0
    fields = ('full_name', )
    show_change_link = True

@admin.register(Students, site=staffadmin_site)
class StudentsRegister(admin.ModelAdmin):
    list_display = ['full_name', '_class']
    search_fields = ['full_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
    
        if request.user.is_superuser:
            return qs
    
        school = School.objects.filter(admin=request.user).first()
        if school:
            return qs.filter(_class__school=school)
    
        return qs.none()
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "_class" and not request.user.is_superuser:
            school = get_staff_school(request)
            kwargs["queryset"] = Classes.objects.filter(school=school) if school else Classes.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)