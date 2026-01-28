from django.core.management.base import BaseCommand
from django.conf import settings
import asyncio

class Command(BaseCommand):
    
    help = "Telegram botni ishga tushurish uchun funksiya"
    def handle(self, *args, **kwargs):
        from bot.runner import start_polling, start_webhook
        if settings.DEBUG:
            try:
                asyncio.run(start_polling())
                self.stdout.write(self.style.WARNING("Bot debug rejimida ishga tushyapti!"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ishga tushishda hatolik: {e}"))
        else:
            try:
                asyncio.run(start_webhook())
                self.stdout.write(self.style.SUCCESS("Bot muvofaqiyatli ishga tushdi!"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ishga tushishda hatolik: {e}"))