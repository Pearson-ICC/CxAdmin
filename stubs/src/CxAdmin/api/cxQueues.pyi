from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects import CxQueue
from typing import Any

class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]: ...
    def get(self) -> Any: ...
