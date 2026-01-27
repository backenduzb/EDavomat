from aiogram import Bot
from config.settings import (
    WEBHOOK_BASE_URL,
    WEBHOOK_SECRET
)

async def set_webhook(bot: Bot) -> None:
    await bot.set_webhook(
        WEBHOOK_BASE_URL,
        secret_token=WEBHOOK_SECRET,
    )
    