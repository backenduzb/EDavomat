from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from bot.database.classes import get_admin_classes
from bot.database.students import get_all_stundets_by_admin


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


async def get_students_by_admin(tg_id: int, class_name: str) -> ReplyKeyboardMarkup:
    students = await get_all_stundets_by_admin(tg_id, class_name)
    
    if not students:
        return ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="O'quvchilar topilmadi")]],
            resize_keyboard=True,
        )

    buttons = [students[i : i + 2] for i in range(0, len(students), 2)]

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=s) for s in row] for row in buttons],
        resize_keyboard=True,
    )
