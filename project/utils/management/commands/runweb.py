import subprocess
import sys

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loyihani ishga tushurish"

    def handle(self, *args, **options):
        workers = getattr(settings, "WORKERS", 2)
        bind = "0.0.0.0:8000"

        if settings.DEBUG:
            self.stdout.write(self.style.WARNING("Debug rejimda ishga tushayapti"))

            try:
                subprocess.run(
                    [sys.executable, "manage.py", "makemigrations"], check=True
                )
                subprocess.run([sys.executable, "manage.py", "migrate"], check=True)

                subprocess.run(
                    [sys.executable, "manage.py", "runserver", bind], check=True
                )
            except:
                pass
            return

        cmd = [
            "gunicorn",
            "config.wsgi:application",
            "--bind",
            bind,
            "--workers",
            str(workers),
        ]

        try:
            subprocess.run(cmd, check=True)
            self.stdout.write(self.style.SUCCESS("Sayt ishga tushurildi!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Saytda hatolik: {e}"))
