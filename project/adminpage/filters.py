from schools.models import School
from django.core.exceptions import ObjectDoesNotExist

def get_staff_school(request):
    if request.user.is_superuser:
        return None
    try:
        return School.objects.get(admin=request.user)
    except ObjectDoesNotExist:
        return None
