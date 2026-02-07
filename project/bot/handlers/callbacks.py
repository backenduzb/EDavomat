from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data == 'reason')
async def get_reason_callback(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    students = data.get('student_name')
    await callback.answer(students, alert=True)