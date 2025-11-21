import asyncio
from aiogram import Bot, Dispatcher
from utils.config import BOT_TOKEN
from handlers import start, callbacks

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(callbacks.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
