from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from app.core.config_reader import BOT_TOKEN

# Routers
from app.handlers import start_router

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

dp.include_router(start_router)