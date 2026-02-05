from django.core.management.base import BaseCommand
from utils.xlsx.writer import write_excel

class Command(BaseCommand):
    help = "Loyihani ishga tushurish"

    def handle(self, *args, **options):
        write_excel(1)