from tabnanny import verbose
from django.db import models

class ClassName(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Sinf nomi"
        verbose_name_plural = "Sinflar nomlari"

class Classes(models.Model):
    updated = models.BooleanField(default=False, verbose_name="Yangilanganmi")
    name = models.ForeignKey(
        ClassName,
        on_delete=models.CASCADE,
        verbose_name="Sinf nomi",
    )
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.SET_NULL,
        verbose_name="Maktab",
        related_name="maktab",
        null=True,
        blank=True,
    )
    teacher_full_name = models.CharField(
        verbose_name="Sinf rahbarni ismi",
        max_length=256,
        null=True,
        blank=True,
    )
    teacher_telegram_id = models.IntegerField(
        verbose_name="Sinf rahbar telegram idsi",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name.name)

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"
