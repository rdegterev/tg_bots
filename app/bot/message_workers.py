from aiogram import types
import asyncio


async def ruby_stick_delete(message):
    stick = message['sticker']
    await asyncio.sleep(message.bot.config.DROP_RUBY_STICK_TIMEOUT)
    if stick['set_name'] == 'RubyToBe' and stick['file_unique_id'] != 'AgADtxQAAp_foUo':
        await message.delete()


async def wordle_delete(message):
    await asyncio.sleep(message.bot.config.DROP_WORDLE_TIMEOUT)
    await message.delete()


async def sorting_hat(message: types.Message):
    pass


async def pin_message(message: types.Message):
    await message.bot.pin_chat_message(chat_id=message.chat.id, message_id=message.message_id)
