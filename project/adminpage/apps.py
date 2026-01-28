from django.apps import AppConfig


class AdminPageConfig(AppConfig):
    name = 'adminpage'
    
    def ready(self):
        from . import admin