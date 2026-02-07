from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def get_choices_button() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Sababli 🟡", callback_data='reason'),
            InlineKeyboardButton(text="Sababsiz 🔴", callback_data='not_reason')
        ],
        [
            InlineKeyboardButton(text="Tugatish ✅", callback_data='finish')
        ]
    ]
    
    return InlineKeyboardMarkup(
        inline_keyboard=buttons,
    )