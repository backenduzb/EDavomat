from django.db import transaction, IntegrityError
from schools.models import School
from classes.models import ClassName, Classes
from students.models import Students
import openpyxl as pyxl

def read_and_write(school_name: str, file_path: str):
    wb = pyxl.load_workbook(file_path)
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
        print("Notog'ri header")
        return None

    school = School.objects.filter(name=school_name).first()
    if not school:
        print("Maktab topilmadi")
        return None

    old_sinf = object()
    class_ = None

    BATCH = 300
    students_batch = []
    links_batch = []  
    
    Through = Classes.students.through

    for row in rows[1:]:
        sinf = row[sinf_col]
        fish = replacer(str(row[fish_col])).strip()

        if not sinf or not fish:
            continue

        if sinf != old_sinf:
            with transaction.atomic():
                try:
                    class_name, _ = ClassName.objects.get_or_create(name=sinf)
                except IntegrityError:
                    class_name = ClassName.objects.get(name=sinf)

                try:
                    class_, _ = Classes.objects.get_or_create(school=school, name=class_name)
                except IntegrityError:
                    class_ = Classes.objects.get(school=school, name=class_name)

            old_sinf = sinf

        students_batch.append(Students(full_name=fish, _class=class_))

        if len(students_batch) >= BATCH:
            created = Students.objects.bulk_create(students_batch)
            links_batch.extend(
                Through(classes_id=class_.id, students_id=s.id) for s in created
            )
            Through.objects.bulk_create(links_batch, ignore_conflicts=True)

            students_batch.clear()
            links_batch.clear()

    if students_batch:
        created = Students.objects.bulk_create(students_batch)
        links_batch.extend(
            Through(classes_id=class_.id, students_id=s.id) for s in created
        )
        Through.objects.bulk_create(links_batch, ignore_conflicts=True)

    return True