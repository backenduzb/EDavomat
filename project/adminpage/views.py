from schools.models import School
from django.shortcuts import get_object_or_404
from classes.models import Statistics
from datetime import date, timedelta
from django.db.models import Count
from django.http import JsonResponse

def statistics_detail(request):
    school = get_object_or_404(School, admin=request.user)

    days = int(request.GET.get("days", 14))
    start = date.today() - timedelta(days=days - 1)
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

    return JsonResponse(
        {
            "school": school.name,
            "range": {"start": start.isoformat(), "end": end.isoformat()},
            "labels": labels,
            "reason": reason_counts,
            "no_reason": noreason_counts,
        }
    )