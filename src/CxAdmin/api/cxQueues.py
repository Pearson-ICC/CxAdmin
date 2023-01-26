from typing import Any
from src.CxAdmin.api import CxItem
from src.CxAdmin.objects import CxQueue


class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]:
        queuesJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        queues = [CxQueue.from_json(queueJson) for queueJson in queuesJson]
        return queues

    def get(self) -> Any:
        raise NotImplementedError()
