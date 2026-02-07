from aiogram.fsm.context import FSMContext

async def add_reason_stundent(full_name: str, state: FSMContext) -> None:
    data = await state.get_data()
    
    students = data.get('reason_students', [])
    students.append(full_name)
    
    await state.update_data(students=students)


async def add_not_reason_stundent(full_name: str, state: FSMContext) -> None:
    data = await state.get_data()
    
    not_students = data.get('nor_reason_students', [])
    not_students.append(full_name)
    
    await state.update_data(not_students=not_students)