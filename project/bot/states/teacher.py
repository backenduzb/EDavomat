from aiogram.fsm.state import State, StatesGroup

class TeacherUpdateState(StatesGroup):
    waiting_student_choice = State()
    waiting_finish = State()