from django.core.management.base import BaseCommand
from django.conf import settings
import asyncio

class Command(BaseCommand):
    
    help = "Telegram botni ishga tushurish uchun funksiya"
    def handle(self, *args, **kwargs):
        from bot.runner import start_polling, start_webhook
        if settings.DEBUG:
            try:
                self.stdout.write(self.style.WARNING("Bot debug rejimida ishga tushyapti!"))
                asyncio.run(start_polling())
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ishga tushishda hatolik: {e}"))
        else:
            try:
                self.stdout.write(self.style.SUCCESS("Bot muvofaqiyatli ishga tushdi!"))
                asyncio.run(start_webhook())
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ishga tushishda hatolik: {e}"))