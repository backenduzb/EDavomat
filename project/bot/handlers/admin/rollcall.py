from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.states.admin import AdminUpdatingClasses
from bot.keyboards.reply.buttons import get_students_by_admin

router = Router()

@router.message(AdminUpdatingClasses.waiting_admin_choice_class, F.text)
async def get_class(message: types.Message, state: FSMContext):
    class_name = message.text.strip()
    await state.set_data({
        'class_name': class_name
    })
    await message.answer("<b>Kelmagan</b> o'quvchilarni tanlang.", reply_markup=await get_students_by_admin(message.from_user.id, class_name))
    await state.set_state(AdminUpdatingClasses.waiting_admin_choice_student)