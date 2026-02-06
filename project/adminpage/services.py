from datetime import date, timedelta

from classes.models import Classes
from django.db.models import Count
from django.shortcuts import get_object_or_404
from schools.models import School
from students.models import Students
from django.db.models import Count, Q
from adminpage.models import Statistics


def get_classes_status(school, stat) -> dict:

    classes = (
        Classes.objects.filter(school=school)
        .select_related("name")
        .annotate(students_count=Count("students", distinct=True))
    )

    reason_map = {}
    noreason_map = {}

    if stat:
        reason_rows = (
            Students.objects.filter(absence_reason_stats=stat)
            .values("_class_id")
            .annotate(cnt=Count("id", distinct=True))
        )
        reason_map = {r["_class_id"]: r["cnt"] for r in reason_rows}

        noreason_rows = (
            Students.objects.filter(absence_no_reason_stats=stat)
            .values("_class_id")
            .annotate(cnt=Count("id", distinct=True))
        )
        noreason_map = {r["_class_id"]: r["cnt"] for r in noreason_rows}

    classes_list = []
    for c in classes:
        classes_list.append(
            {
                "id": c.id,
                "name": c.name.name,
                "students_count": c.students_count,
                "reason_absent": reason_map.get(c.id, 0),
                "no_reason_absent": noreason_map.get(c.id, 0),
            }
        )
    return {
        "classes_count": classes.count(),
        "updated_classes": classes.filter(updated=True).count(),
        "unupdated_classes": classes.filter(updated=False).count(),
        "classes": classes_list,
        "has_statistics": bool(stat),
    }

def statistics_detail(school) -> dict:

    start = date.today() - timedelta(days=30)
    end = date.today()

    qs = (
        Statistics.objects.filter(school=school, created_at__range=(start, end))
        .annotate(
            reason_cnt=Count("reason_students", distinct=True),
            noreason_cnt=Count("no_reason_students", distinct=True),
        )
        .order_by("created_at")
    )

    labels = []
    reason_counts = []
    noreason_counts = []

    data_map = {s.created_at: (s.reason_cnt, s.noreason_cnt) for s in qs}

    cur = start
    while cur <= end:
        r, nr = data_map.get(cur, (0, 0))
        labels.append(cur.strftime("%Y-%m-%d"))
        reason_counts.append(r)
        noreason_counts.append(nr)
        cur += timedelta(days=1)

    return {
        "school": school.name,
        "range": {"start": start.isoformat(), "end": end.isoformat()},
        "labels": labels,
        "reason": reason_counts,
        "no_reason": noreason_counts,
    }


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
        k_protcent = f"{((100 / students_count) * kelganlar):.1f}"
        km_protcent = f"{((100 / students_count) * kelmaganlar):.1f}"
    else:
        k_protcent = "0"
        km_protcent = "0"

    diagram_data = statistics_detail(school)
    classes_data = get_classes_status(school, statistics)

    return {
        "school_name": school.name,
        "school_statisticks": {
            "students_count": students_count,
            "classes_count": classes_count,
            "kelmaganlar": kelmaganlar,
            "kelganlar": kelganlar,
            "k_protcent": k_protcent,
            "km_protcent": km_protcent,
        },
        "diagram_info": diagram_data,
        "classes_data": classes_data,
    }
