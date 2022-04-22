from aiogram import Dispatcher, types
from bot.message_workers import ruby_stick_delete, wordle_delete, sorting_hat



async def add_handlers(dispatcher):
    dispatcher.register_message_handler(ruby_stick_delete, content_types=types.ContentTypes.STICKER)
    dispatcher.register_message_handler(sorting_hat, commands=['choice_me'])
    dispatcher.register_message_handler(wordle_delete, [lambda msg: msg.text.lower() == 'cancel'])