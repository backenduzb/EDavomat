from django.db import models

class Statistics(models.Model):
    reason_students = models.ManyToManyField(
        "students.Students",
        verbose_name="Sababli kelgan o'quvchilar",
        related_name="statistics_reason",
    )
    no_reason_students = models.ManyToManyField(
        "students.Students",
        verbose_name="Sababsiz kelgan o'quvchilar",
        related_name="statistics_no_reason",
    )
    _class = models.ForeignKey(
        "classes.Classes", on_delete=models.CASCADE, verbose_name="Sinf"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilingan vaqt")

    class Meta:
        verbose_name = "Statistik"
        verbose_name_plural = "Statislikalar"


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
        verbose_name="Sing nomi",
    )
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
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
    students = models.ManyToManyField(
        "students.Students", verbose_name="O'quvchilar", related_name="oquvchi"
    )

    def __str__(self):
        return str(self.name.name)

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"
