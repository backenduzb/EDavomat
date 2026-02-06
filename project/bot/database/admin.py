from channels.models.admins import BotAdmin
from classes.models import Classes
from asgiref.sync import sync_to_async

@sync_to_async
def check_is_admin(tg_id: int) -> bool:
    return BotAdmin.objects.filter(admin_tg_id=tg_id).exists()

@sync_to_async
def get_admin_classes(tg_id: int) -> list:
    admin = BotAdmin.objects.filter(admin_tg_id=tg_id).first()
    if not admin:
        return []
    
    classes = list(
        Classes.objects
        .filter(school=admin.school)
        .values_list('name__name', flat=True)   
    )
    return classes

