from django.contrib import admin
from django.contrib.admin import AdminSite
from django.templatetags.static import static
from .models import Statistics
from django.db.models import Count
from .services import dashboard_data


@admin.register(Statistics)
class StatisticsRegister(admin.ModelAdmin):
    list_display = ("created_at", "school", "reason_students_count", "no_reason_students_count")
    readonly_fields = ('created_at',)
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

class SuperAdmin(AdminSite):
    site_header = "Super admin"
    site_title = "Super admin"
    index_title = "Boshqaruv"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser


class StaffAdmin(AdminSite):
    site_header = "Maktab admin"
    site_title = "Maktab admin"
    index_title = "Boshqaruv"

    index_template = "staffadmin/index.html"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff and not request.user.is_superuser

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(dashboard_data(request))

        return super().index(request, extra_context=extra_context)


superadmin_site = SuperAdmin(name="superadmin")
staffadmin_site = StaffAdmin(name="staffadmin")

admin.autodiscover()


def merge_into_super(site) -> None:
    for model, model_admin in site._registry.items():
        try:
            superadmin_site.register(model, model_admin.__class__)
        except admin.sites.AlreadyRegistered:
            pass


merge_into_super(admin.site)
merge_into_super(staffadmin_site)
