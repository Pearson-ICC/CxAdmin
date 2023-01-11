from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxQueue import CxQueue


class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]:
        queuesJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        queues = [CxQueue.from_json(queueJson) for queueJson in queuesJson]
        return queues
