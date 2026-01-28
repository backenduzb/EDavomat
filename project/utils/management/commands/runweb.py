from django.core.management.base import BaseCommand
from django.conf import settings
import subprocess
import sys

class Command(BaseCommand):
    help = "Loyihani ishga tushurish"
    
    def handle(self, *args, **options):
        workers = settings.WORKERS
        bind = "0.0.0.0:8000"
        
        if settings.DEBUG:
            self.stdout.write(
                self.style.WARNING("Debug rejimda ishga tushayapti")
            )
            subprocess.run(
                [sys.executable, "manage.py", "runserver", "0.0.0.0:8000"],
                check=True
            )

            return*
        
        cmd = [
            "gunicorn",
            "config.wsgi:application",
            "--bind", bind,
            "--workers", str(workers),
        ]
        
        cmd = [c for c in cmd if c] 
        try:        
            subprocess.run(cmd, check=True)
            self.stdout.write(self.style.SUCCESS("Sayt ishga tushurildi!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Saytda hatolik: {e}"))