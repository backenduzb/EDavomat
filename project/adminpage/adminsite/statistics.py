from django.contrib import admin 
from adminpage.models import Statistics
from django.db.models import Count
from adminpage.admin import staffadmin_site

@admin.register(Statistics, site=staffadmin_site)
class StatisticsRegister(admin.ModelAdmin):
    list_display = ("created_at", "school", "reason_students_count", "no_reason_students_count")
    readonly_fields = ("created_at",)

    def get_queryset(self, request):
        qs = super().get_queryset(request).annotate(
            reason_cnt=Count("reason_students", distinct=True),
            noreason_cnt=Count("no_reason_students", distinct=True),
        )

        if request.user.is_superuser:
            return qs

        school = get_staff_school(request)
        return qs.filter(school=school) if school else qs.none()

    @admin.display(description="Sababli (count)")
    def reason_students_count(self, obj):
        return obj.reason_cnt

    @admin.display(description="Sababsiz (count)")
    def no_reason_students_count(self, obj):
        return obj.noreason_cnt

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        school = get_staff_school(request)

        if db_field.name == "school":
            kwargs["queryset"] = School.objects.filter(id=school.id) if school else School.objects.none()

        if db_field.name == "_class":
            kwargs["queryset"] = Classes.objects.filter(school=school) if school else Classes.objects.none()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name in ("reason_students", "no_reason_students"):
            if request.user.is_superuser:
                obj_id = request.resolver_match.kwargs.get("object_id")
                stat = Statistics.objects.select_related("school").filter(pk=obj_id).first() if obj_id else None
                if stat and stat.school_id:
                    kwargs["queryset"] = Students.objects.filter(_class__school_id=stat.school_id)
                else:
                    kwargs["queryset"] = Students.objects.none()
                return super().formfield_for_manytomany(db_field, request, **kwargs)

            school = get_staff_school(request)
            kwargs["queryset"] = Students.objects.filter(_class__school=school) if school else Students.objects.none()

        return super().formfield_for_manytomany(db_field, request, **kwargs)