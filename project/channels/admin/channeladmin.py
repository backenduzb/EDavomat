from adminpage.admin import staffadmin_site
from adminpage.filters import get_staff_school
from django.contrib import admin

from channels.models.channels import Channels


@admin.register(Channels, site=staffadmin_site)
class ChannelsRegister(admin.ModelAdmin):
    list_display = ["tg_group_username", "tg_group_id", "school"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        school = get_staff_school(request)
        return qs.filter(school=school) if school else qs.none()

    def get_readonly_fields(self, request, obj=None):
        ro = list(super().get_readonly_fields(request, obj))
        if not request.user.is_superuser:
            ro += ["school"]
        return ro

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.school = get_staff_school(request)
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        if not request.user.is_staff:
            return False

        school = get_staff_school(request)
        if not school:
            return False

        exists = Channels.objects.filter(school=school).exists()
        return not exists

    def has_change_permission(self, request, obj=None):
        perm = super().has_change_permission(request, obj=obj)
        if request.user.is_superuser or obj is None:
            return perm
        school = get_staff_school(request)
        return perm and school and obj.school_id == school.id
