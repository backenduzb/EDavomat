from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application 
from aiogram import Bot, Dispatcher
from bot.utils.webhook import set_webhook
from bot.config.settings import (
    DEFAULT_BOT_PROPERTIES,
    WEB_SERVER_PORT,
    WEB_SERVER_HOST,
    WEBHOOK_SECRET,
    BOT_TOKEN,
)
from bot.config.routers import ROUTERS
from aiohttp import web

dp = Dispatcher()
dp.include_routers(*ROUTERS)
bot = Bot(
    token=BOT_TOKEN,
    default=DEFAULT_BOT_PROPERTIES,
)

async def start_polling() -> None:
    global dp, bot
    import logging
    import sys
    
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

async def start_webhook():
    dp.startup.register(set_webhook)
    
    app = web.Application()
    
    webhook_handlers = SimpleRequestHandler(
        secret_token=WEBHOOK_SECRET,
        dispatcher=dp,
        bot=bot,
    )
    webhook_handlers.register(app, path="/webhook")
    
    setup_application(app, dp, bot=bot)
    web.run_app(
        app,
        host=WEB_SERVER_HOST,
        port=WEB_SERVER_PORT,
    )