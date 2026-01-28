from django.db import models

class ClassName(models.Model):
    name = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = "Sinf nomi"
        verbose_name_plural = "Sinflar nomlari"

class Classes(models.Model):
    updated = models.BooleanField(default=False, verbose_name='Yangilanganmi')
    name = models.ForeignKey(
        ClassName,
        on_delete=models.CASCADE,
        verbose_name="Sing nomi",
    )
    teacher_full_name = models.CharField(
        verbose_name="Sinf rahbarni ismi",
        max_length=256,
    )
    teacher_telegram_id = models.IntegerField(verbose_name="Sinf rahbar telegram idsi")
    students = models.ManyToManyField(
        "students.Students",
        verbose_name="O'quvchilar",
        related_name="oquvchi"
    )
    
    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"