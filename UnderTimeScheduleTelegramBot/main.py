import asyncio
from aiogram import Bot, Dispatcher, executor
from config import botToken

loop = asyncio.get_event_loop()
bot = Bot(botToken, parse_mode="HTML")
ourDispatcher = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import ourDispatcher, startupMessage
    executor.start_polling(ourDispatcher, on_startup=startupMessage)