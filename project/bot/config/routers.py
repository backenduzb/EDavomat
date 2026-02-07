from bot.handlers import start
from bot.handlers.admin import rollcall

ROUTERS = [
    start.router,
    rollcall.router,
]