from django.contrib import admin
from .models import Statistics
from django.db.models import Count
from .filters import get_staff_school
from students.models import Students
from adminpage.adminsite.sites import *

superadmin_site = SuperAdmin(name="superadmin")
staffadmin_site = StaffAdmin(name="staffadmin")

admin.autodiscover()

_original_admin_register = admin.site.register

def _register_with_superadmin(model_or_iterable, admin_class=None, **options):
    _original_admin_register(model_or_iterable, admin_class, **options)
    try:
        superadmin_site.register(model_or_iterable, admin_class, **options)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.register = _register_with_superadmin

def merge_into_super(site):
    for model, model_admin in site._registry.items():
        try:
            superadmin_site.register(model, model_admin.__class__)
        except admin.sites.AlreadyRegistered:
            pass


merge_into_super(admin.site)
merge_into_super(staffadmin_site)
