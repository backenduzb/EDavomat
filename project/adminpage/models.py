from django.db import models

class Statistics(models.Model):
    school = models.ForeignKey(
        "schools.School",
        verbose_name="Maktab",
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    reason_students = models.ManyToManyField(
        "students.Students",
        verbose_name="Sababli kelgan o'quvchilar",
        related_name="absence_reason_stats",
        blank=True,
    )
    no_reason_students = models.ManyToManyField(
        "students.Students",
        verbose_name="Sababsiz kelgan o'quvchilar",
        related_name="absence_no_reason_stats",
        blank=True
    )
    created_at = models.DateField(verbose_name="Yaratilingan vaqt")
    
    def __str__(self):
        return str(self.created_at)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["school", "created_at"], name="uniq_school_day")
        ]
        verbose_name = "Statistik"
        verbose_name_plural = "Statislikalar"
