from asgiref.sync import sync_to_async
from channels.models.admins import BotAdmin
from classes.models import Classes


@sync_to_async(thread_sensitive=False)
def check_is_admin(tg_id: int) -> tuple:
    teacher = (
        Classes.objects.filter(teacher_telegram_id=tg_id)
        .values_list("teacher_full_name", flat=True)
        .first()
    )
    is_admin = BotAdmin.objects.filter(admin_tg_id=tg_id).exists()
    return (teacher is not None, is_admin, teacher)
