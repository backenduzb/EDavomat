from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.database.admin import get_admin_classes


async def classes_buttons(tg_id: int) -> ReplyKeyboardMarkup:
    classes = await get_admin_classes(tg_id)
    if not classes:
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Sinflar topilmadi")]],
            resize_keyboard=True,
        )

    buttons = [classes[i : i + 5] for i in range(0, len(classes), 5)]
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=s) for s in row] for row in buttons],
        resize_keyboard=True,
    )
    return keyboard
