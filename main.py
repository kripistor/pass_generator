import asyncio
from aiogram import Bot, Dispatcher
from handlers import start
from config import token

# Запуск бота
async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(start.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())