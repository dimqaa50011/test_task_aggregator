from datetime import datetime, timedelta
from calendar import monthrange

from ..storage.base import BaseStorage


class Aggregator:
    def __init__(self, storage: BaseStorage) -> None:
        self._storage = storage

    async def get_data(self, dt_from: str, dt_upto: str, group_type: str):
        dt_from = datetime.fromisoformat(dt_from)
        dt_upto = datetime.fromisoformat(dt_upto)
        docs = await self._storage.get_many(dt_from, dt_upto)

        return await self._get_result(dt_from, dt_upto, docs, group_type)

    async def _get_result(
        self, dt_from: datetime, dt_to: datetime, docs: list[dict], group_type: str
    ):
        dt_start = dt_from
        res = {"dataset": [], "labels": []}
        while True:

            if group_type == "hour":
                coeff = 1
            elif group_type == "day":
                coeff = 24
            elif group_type == "month":
                coeff = 24 * monthrange(dt_start.year, dt_start.month)[1]
            _dt_end = dt_start + timedelta(hours=1 * coeff)

            answer = await self._get_docs_by_period(dt_start, _dt_end, docs)

            res["dataset"].append(sum([item["value"] for item in answer]))
            res["labels"].append(
                datetime(
                    dt_start.year,
                    dt_start.month,
                    day=dt_start.day,
                    hour=dt_start.hour,
                    tzinfo=dt_start.tzinfo,
                ).isoformat()
            )

            if _dt_end > dt_to:
                break

            dt_start = _dt_end

        return res

    async def _get_docs_by_period(
        self, dt_from: datetime, dt_upto: datetime, docs: list[dict]
    ):
        def _filter(item: dict):
            dt: datetime = item.get("dt")
            dt = datetime(
                year=dt.year,
                month=dt.month,
                hour=dt.hour,
                minute=dt.minute,
                day=dt.day,
                second=dt.second,
                tzinfo=dt_from.tzinfo,
            )
            return dt >= dt_from and dt < dt_upto

        return list(filter(_filter, docs))
