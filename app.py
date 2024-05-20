import asyncio
import json

from aiogram import Bot, Dispatcher, types, Router

from src.config.settings import app_settings
from src.aggregator.aggregator import Aggregator
from src.storage.default import DefaultStorage
from src.config.mongo import sample_collection

aggregator = Aggregator(DefaultStorage(sample_collection))
router = Router()


@router.message()
async def handler(message: types.Message):
    data = json.loads(message.text)
    res = await aggregator.get_data(
        dt_from=data["dt_from"], dt_upto=data["dt_upto"], group_type=data["group_type"]
    )
    await message.answer(json.dumps(res))


async def startup():
    bot = Bot(token=app_settings.bot.token)
    dp = Dispatcher()

    dp.include_router(router)
    
    await dp.start_polling(bot)
        


if __name__ == "__main__":
    asyncio.run(startup())
