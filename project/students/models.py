from django.db import models

class Students(models.Model):
    full_name = models.CharField(max_length=256, verbose_name="O'quvchining ismi")
    _class = models.ForeignKey(
        "classes.Classes",
        on_delete=models.SET_NULL,
        verbose_name="O'quvchining sinfi",
        related_name='students',
        null=True,
        blank=True,
    )
    sababi = models.TextField(verbose_name="Sababi", blank=True, null=True)
    
    def __str__(self):
        return str(self.full_name)
    
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"