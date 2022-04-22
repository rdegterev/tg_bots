from aiogram import types
import asyncio

async def ruby_stick_delete(message: types.Message):
    stick = message['sticker']
    await asyncio.sleep(message.bot.config.DROP_RUBY_STICK_TIMEOUT)
    if stick['set_name'] == 'RubyToBe' and stick['file_unique_id'] != 'AgADtxQAAp_foUo':
        await message.delete()


async def wordle_delete(message: types.Message):
    await asyncio.sleep(message.bot.config.DROP_WORDLE_TIMEOUT)
    await message.delete()


async def sorting_hat(message: types.Message):
    pass