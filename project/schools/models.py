from django.contrib.auth.models import User
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=128, verbose_name="Maktab nomi", unique=True)
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Maktab direktori profili",
        related_name="admins",
    )
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Maktab"
        verbose_name_plural = "Maktablar"
