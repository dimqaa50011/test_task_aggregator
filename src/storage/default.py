from datetime import datetime
from .base import BaseStorage

class DefaultStorage(BaseStorage):
    async def get_many(self, db_from: datetime, dt_upto: datetime):
        cursor = self._collecion.find(
            {"dt": {"$gte": db_from, "$lte": dt_upto}}
        )
        return await cursor.to_list(length=await self._collecion.count_documents({}))
    