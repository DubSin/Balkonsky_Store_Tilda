import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import start, currency_calculator, course
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(start.router, currency_calculator.router, course.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())