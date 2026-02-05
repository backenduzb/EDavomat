from django.http import JsonResponse
from utils.xlsx.reader import read_and_write
from django.views.decorators.http import require_POST
from schools.models import School

@require_POST
def upload_students_excel(request):
    file = request.FILES.get("file")
    if not file:
        return JsonResponse({"ok": False, "error": "Fayl yuborilmadi"}, status=400)

    school = School.objects.filter(admin=request.user).first()
    if not school:
        return JsonResponse({"ok": False, "error": "school_name kerak"}, status=400)

    ok = read_and_write(school, file)
    if not ok:
        return JsonResponse({"ok": False, "error": "Excel format yoki header noto'g'ri"}, status=400)

    return JsonResponse({"ok": True})