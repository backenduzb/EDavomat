from django.db import transaction, IntegrityError
from schools.models import School
from classes.models import ClassName, Classes
from students.models import Students
import openpyxl as pyxl
from utils.string.uzlatin import replacer

def read_and_write(school, uploaded_file):
    wb = pyxl.load_workbook(uploaded_file)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return None

    headers = rows[0]

    fish_alias = {"FISH", "F.I.SH", "F.I.Sh", "fish", "I.F.Sh"}
    sinf_alias = {"SINF", "sinf", "SINFI", "sinfi", "Sinf"}

    fish_col = None
    sinf_col = None

    for i, h in enumerate(headers):
        if h in fish_alias:
            fish_col = i
        if h in sinf_alias:
            sinf_col = i

    if fish_col is None or sinf_col is None:
        return None

    if not school:
        return None

    old_sinf = object()
    class_ = None

    BATCH = 300
    students_batch = []

    for row in rows[1:]:
        sinf = row[sinf_col]
        fish = replacer(str(row[fish_col])).strip()

        if not sinf or not fish:
            continue

        if sinf != old_sinf:
            with transaction.atomic():
                class_name, _ = ClassName.objects.get_or_create(name=sinf)
                class_, _ = Classes.objects.get_or_create(school=school, name=class_name)
            old_sinf = sinf

        students_batch.append(Students(full_name=fish, _class=class_))

        if len(students_batch) >= BATCH:
            Students.objects.bulk_create(students_batch)
            students_batch.clear()

    if students_batch:
        Students.objects.bulk_create(students_batch)

    return True
