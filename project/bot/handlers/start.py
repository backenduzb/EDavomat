from aiogram import types, Router, F

router = Router()

@router.message(F.text=="/start")
async def start(message: types.Message):
    await message.answer("Salom")