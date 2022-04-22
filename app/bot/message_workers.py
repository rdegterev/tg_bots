from aiogram import types
import asyncio

async def ruby_stick_delete(message: types.Message):
    stick = message['sticker']
    await asyncio.sleep(message.bot.config.DROP_RUBY_STICK_TIMEOUT)
    if stick['set_name'] == 'RubyToBe' and stick['file_unique_id'] != 'AgADtxQAAp_foUo':
        await message.delete()


async def wordle_delete(message: types.Message):
    await asyncio.sleep(message.bot.config.DROP_WORDLE_TIMEOUT)
    text = message.text
    enc = text.encode()
    if 'wordle' in text or b'\xe2\xac\x9c\xef\xb8\x8f' in enc or b'\xf0\x9f\x9f\xa9' in enc or b'\xf0\x9f\x9f\xa8' in enc:
        await message.delete()


async def sorting_hat(message: types.Message):
    resp = await message.bot.aio_session.get('https://statsapi.web.nhl.com/api/v1/game/2021021230/boxscore', ssl=False)
    # print((await resp.json()).keys())
    await message.answer((await resp.json()).get('copyright'))