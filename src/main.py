import asyncio
from aiogram import Bot, Dispatcher

from src.handlers import router
from src.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token='6887887112:AAEmoPkNbLt3IeJGphUU2MFHnmxIix1rgBU')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
