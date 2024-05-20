from datetime import datetime
from .base import BaseStorage

class DefaultStorage(BaseStorage):
    async def get_many(self, db_from: datetime, dt_upto: datetime):
        cursor = self._collecion.find(
            {"dt": {"$lte": db_from, "$gte": dt_upto}}
        )
        return await cursor.to_list(length=await self._collecion.count_documents({}))
    