from django.db import models

class BotAdmin(models.Model):
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="bot_admins",
        verbose_name="Maktab",
    )
    admin_tg_id = models.BigIntegerField(unique=True, verbose_name="Adminning telegram IDsi")
    admin_username = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name="Telegram username"
    )

    def __str__(self):
        return str(self.admin_username) or str(self.admin_tg_id)

    class Meta:
        verbose_name = "Botdagi admin"
        verbose_name_plural = "Botdagi adminlar"
