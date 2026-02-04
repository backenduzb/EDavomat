from datetime import date
from tracemalloc import Statistic

from classes.models import Classes, Statistics
from django.shortcuts import get_object_or_404
from schools.models import School
from students.models import Students


def dashboard_data(request) -> dict:
    now = date.today()
    school = get_object_or_404(School, admin=request.user)
    classes_count = Classes.objects.filter(school=school).count()
    students_count = Students.objects.filter(_class__school=school).count()
    statistics, _ = Statistics.objects.get_or_create(created_at=now, school=school)
    kelmaganlar = (
        statistics.reason_students.count() + statistics.no_reason_students.count()
    )
    kelganlar = students_count - kelmaganlar
    if students_count > 0:
        k_protcent = f"{((100 / students_count) * kelganlar):.1f}%"
        km_protcent = f"{((100 / students_count) * kelmaganlar):.1f}%"
    else:
        k_protcent = "0%"
        km_protcent = "0%"

    return {
        "school_name": school.name,
        "school_statisticks": [
            {
                "students_count": students_count,
                "classes_count": classes_count,
                "kelmaganlar": kelmaganlar,
                "kelganlar": kelganlar,
                "k_protcent": k_protcent,
                "km_protcent": km_protcent,
            }
        ],
    }

