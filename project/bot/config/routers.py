from bot.handlers import start
from bot.handlers.admin import rollcall
from bot.handlers import callbacks
from bot.handlers.teacher import rollcall as teacher_rollcall_handler

ROUTERS = [
    start.router,
    callbacks.router,
    teacher_rollcall_handler.router,
]