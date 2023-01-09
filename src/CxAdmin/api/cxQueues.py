from typing import Any
from api.cxItem import CxItem
from objects.cxQueue import CxQueue


class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]:
        queuesJson: list[dict[str, Any]] = self._httpClient.get(self._path)
        queues = [CxQueue.from_json(queueJson) for queueJson in queuesJson]
        return queues
