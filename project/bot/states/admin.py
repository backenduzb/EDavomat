from aiogram.fsm.state import (
    State, StatesGroup
)

class AdminUpdatingClasses(StatesGroup):
    waiting_admin_choice_class = State()
    waiting_admin_choice_student = State()
    waiting_admin_finish = State()