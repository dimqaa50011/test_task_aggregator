from motor.motor_asyncio import AsyncIOMotorCollection


class BaseStorage:
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self._collecion = collection

    async def get_many(self, *args, **kwargs):
        raise NotImplementedError
