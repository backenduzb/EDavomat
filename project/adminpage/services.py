from django.shortcuts import get_object_or_404
from schools.models import School


def dashboard_data(request) -> dict:
    school = get_object_or_404(School, admin=request.user)

    return {"school_name": school.name, "others": [{"text": "salom"}]}
