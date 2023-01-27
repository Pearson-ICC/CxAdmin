from typing import Any
from CxAdmin.api.http.httpClientModel import HTTPClientModel
from CxAdmin.objects.__cxQueue import CxQueue


class CxQueues:
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    def getQueues(self) -> list[CxQueue]:
        queuesJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        queues = [CxQueue.from_json(queueJson) for queueJson in queuesJson]
        return queues

    def get(self) -> list[CxQueue]:
        return self.getQueues()

    def getActiveQueues(self) -> list[CxQueue]:
        queues = self.getQueues()
        activeQueues = [queue for queue in queues if queue.active]
        return activeQueues
