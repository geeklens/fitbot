import asyncio
from app.core.bot import bot, dp

async def main():
    print("🚀 Бот запускается...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка во время работы бота: {e}")
    finally:
        await bot.session.close()
        print("🔌 Соединение с Telegram закрыто.")

if __name__ == "__main__":
    try:
        print("🔄 Инициализация asyncio...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Бот остановлен вручную (Ctrl+C). До встречи!")
