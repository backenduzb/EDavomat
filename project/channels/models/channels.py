from django.db import models

class Channels(models.Model):
    school = models.OneToOneField(
        "schools.School",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="tg_channel",
        verbose_name="Maktab",
    )
    tg_group_id = models.BigIntegerField(unique=True, verbose_name="Telegram guruh IDsi")
    tg_group_username = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name="Telegram username"
    )

    def __str__(self):
        return str(self.tg_group_username) or str(self.tg_group_id)

    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"