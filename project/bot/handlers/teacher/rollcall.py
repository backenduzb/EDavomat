from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from bot.keyboards.reply.buttons import get_students_by_admin
from bot.keyboards.inline.buttons import get_choices_button
from bot.states.teacher import TeacherUpdateState

router = Router()

@router.message(TeacherUpdateState.waiting_student_choice)
async def get_students_handler(message: types.Message, state: FSMContext):
    student_name = message.text.strip()
    await state.set_data({"student_name": student_name})
    await message.answer(
        f"{student_name} nima sabab bilan kelmadi?",
        reply_markup=await get_choices_button() 
    )
