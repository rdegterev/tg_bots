from aiogram import Dispatcher, types
from bot.message_workers import ruby_stick_delete, wordle_delete, sorting_hat



async def add_handlers(dispatcher):
    dispatcher.register_message_handler(ruby_stick_delete, content_types=types.ContentTypes.STICKER)
    dispatcher.register_message_handler(sorting_hat, commands=['choice_me'])
    dispatcher.register_message_handler(wordle_delete, lambda msg: 'wordle' in msg.text.lower() \
                                                                    or b'\xe2\xac\x9c\xef\xb8\x8f' in msg.text.encode() \
                                                                    or b'\xf0\x9f\x9f\xa9' in msg.text.encode() \
                                                                    or b'\xf0\x9f\x9f\xa8' in msg.text.encode())