from datetime import datetime
from tracemalloc import Statistic

from classes.models import Classes, Statistics
from django.shortcuts import get_object_or_404
from schools.models import School
from students.models import Students


def dashboard_data(request) -> dict:
    now = datetime.now().strftime("%Y-%m-%d")
    school = get_object_or_404(School, admin=request.user)
    classes_count = Classes.objects.filter(school=school).count()
    students_count = Students.objects.filter(_class__school=school).count()
    statistics = Statistics.objects.filter(created_at=now, school=school).first()
    kelmaganlar = (
        statistics.reason_students.count() + statistics.no_reason_students.count()
    )
    kelganlar = students_count - kelmaganlar
    k_protcent = f"{((100 / students_count) * kelganlar):.1f}%"
    km_protcent = f"{((100 / students_count) * kelmaganlar):.1f}%" 
    
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
