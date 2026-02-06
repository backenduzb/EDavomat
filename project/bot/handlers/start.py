from aiogram import types, Router, F
from bot.database.admin import check_is_admin
from bot.keyboards.reply.buttons import classes_buttons

router = Router()

@router.message(F.text=="/start")
async def start(message: types.Message):
    checker = await check_is_admin(message.from_user.id)
    
    if checker:
        await message.answer(
            f"Assalomu alaykum {message.from_user.full_name}",
            reply_markup=await classes_buttons(message.from_user.id),
        )
        