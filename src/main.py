import os
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher

from src.database.models import async_main
from src.handlers import router


async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
