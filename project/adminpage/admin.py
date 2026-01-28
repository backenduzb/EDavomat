from django.contrib import admin
from django.contrib.admin import AdminSite

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
    
    def has_permission(self, request):
        return request.user.is_active and (request.user.is_staff or request.user.is_superuser)

superadmin_site = SuperAdmin(name="superadmin")
staffadmin_site = StaffAdmin(name="staffadmin")

admin.autodiscover()

def merge_into_super(site):
    for model, model_admin in site._registry.items():
        try:
            superadmin_site.register(model, model_admin.__class__)
        except admin.sites.AlreadyRegistered:
            pass

merge_into_super(admin.site)
merge_into_super(staffadmin_site)
