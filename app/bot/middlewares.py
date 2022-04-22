import asyncio
from logging import getLogger

import aiohttp
import asyncpg

# from app.dataclasses import Queues, Cache
# from app.tasks import send_cats


async def setup_middlewares(bot, first_start = False):
    # dispatcher.queues = Queues()
    # dispatcher.cache = Cache()
    bot.logger = getLogger(name='sorting_hat')
    bot.aio_session = aiohttp.ClientSession()
    bot.database = await asyncpg.connect(dsn=bot.config.DATABASE_URI)
    # asyncio.create_task(send_cats(dispatcher))

    if first_start:
        await bot.database.
