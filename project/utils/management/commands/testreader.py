from django.core.management.base import BaseCommand
from utils.xlsx.reader import read_and_write

class Command(BaseCommand):
    help = "Loyihani ishga tushurish"

    def handle(self, *args, **options):
            read_and_write(school_name="Kattaqo'rg'on tuman IM")