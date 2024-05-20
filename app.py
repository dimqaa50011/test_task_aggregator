import asyncio
from datetime import datetime

from src.config.settings import app_settings
from src.storage.default import DefaultStorage
from src.config.mongo import sample_collection
from src.aggregator.aggregator import Aggregator

async def start():
    ds = DefaultStorage(sample_collection)
    aggr = Aggregator(ds)
    res = await aggr.get_data("2022-10-01T00:00:00", "2022-11-30T23:59:00", "day")
    # res = await ds.get_many(datetime.fromisoformat("2022-01-01T03:28:00.000+00:00"), datetime.fromisoformat("2021-12-31T23:50:00.000+00:00"))
    print(res)
    print()

asyncio.run(start())