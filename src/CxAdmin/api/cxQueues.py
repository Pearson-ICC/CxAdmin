import json
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxQueue import CxQueue


class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]:
        queuesJson: str = self._httpClient.get(self._path)
        queues = [
            CxQueue.from_json(json.loads(queueJson)["result"])
            for queueJson in queuesJson
        ]
        return queues
