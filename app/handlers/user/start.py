from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from app.keyboards import getLang

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Привет! / Hello! / Salom!\n\n"
        "🤖 Я фитнес-бот, который поможет тебе начать путь к лучшей версии себя!\n\n"
        "🌍 Пожалуйста, выбери язык общения:\n"
        "🇷🇺 Для русского — нажми Русский\n"
        "🇬🇧 For English — tap English\n"
        "🇺🇿 O‘zbekcha — tanlang O‘zbek",
        reply_markup=getLang()
    )
