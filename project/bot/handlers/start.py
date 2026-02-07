from aiogram import types, Router, F
from bot.database.admin import check_is_admin
from bot.keyboards.reply.buttons import classes_buttons
from aiogram.fsm.context import FSMContext
from bot.states.admin import AdminUpdatingClasses
from bot.states.teacher import TeacherUpdateState

router = Router()

@router.message(F.text=="/start")
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    is_teacher, is_admin, teacher_name = await check_is_admin(message.from_user.id)
    
    if is_teacher or is_admin:
        if is_admin:
            await message.answer(
                f"Assalomu alaykum {message.from_user.full_name} davomat topshirmoqchi bolgan sinfingizni tanlang.",
                reply_markup=await classes_buttons(message.from_user.id),
            )
            await state.set_state(AdminUpdatingClasses.waiting_admin_choice_class)
            
        if is_teacher:
            await message.answer(
                f"Assalomu alaykum {teacher_name} davomat topshirmoqchi bolgan sinfingizni tanlang.",
                reply_markup=await classes_buttons(message.from_user.id),
            )
            await state.set_state(TeacherUpdateState.waiting_student_choice)
    else:
        await message.answer(
            f"Assalomu alaykum <b>{message.from_user.full_name}</b>, siz hozircha hech qaysi maktabda ustoz emassiz! \n\n<b>Sizning telegram ID:</b> <code>{message.from_user.id}</code>"
        )