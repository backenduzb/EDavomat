from asgiref.sync import sync_to_async
from channels.models.admins import BotAdmin
from classes.models import Classes
from students.models import Students


@sync_to_async(thread_sensitive=False)
def get_all_stundets_by_teacher(tg_id: int) -> list:
    class_ = (
        Classes.objects.filter(teacher_telegram_id=tg_id)
        .values_list("teacher_full_name", flat=True)
        .first()
    )
    students = list(
        Students.objects
        .filter(_class=class_)
        .values_list("full_name", flat=True)
    )
    return students


@sync_to_async(thread_sensitive=False)
def get_all_stundets_by_admin(tg_id: int, class_name: str) -> list:
    admin = BotAdmin.objects.filter(admin_tg_id=tg_id).first()
    class_ = Classes.objects.filter(school=admin.school, name__name=class_name).first()
    students = list(
        Students.objects
        .filter(_class=class_)
        .values_list("full_name", flat=True)
    )

    return students
