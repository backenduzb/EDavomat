from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = "Debug rejimi uchun avto admin yaratish commandi."
    
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="superadmin").exists() and settings.DEBUG:
            User.objects.create_superuser(
                username="superadmin",
                password="superadmin02"
            )
            self.stdout.write(self.style.SUCCESS("User yaratildi!"))
            return
        else:
            self.stdout.write(self.style.ERROR("User yaratilmadi!"))
            return