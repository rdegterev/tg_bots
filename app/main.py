import asyncio

from aiogram import Bot, Dispatcher, executor

from bot.settings import Settings
from bot.middlewares import setup_middlewares
from bot.handlers import add_handlers

settings = Settings()
bot = Bot(token=settings.TELEGRAM_API_TOKEN)
bot.config = settings
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
dispatcher = Dispatcher(bot=bot, loop=loop)


async def before_start(dispatcher: Dispatcher):
    dispatcher.config = settings
    await setup_middlewares(dispatcher.bot)
    await add_handlers(dispatcher)


if __name__ == '__main__':
    loop.run_until_complete(before_start(dispatcher))
    executor.start_polling(dispatcher)