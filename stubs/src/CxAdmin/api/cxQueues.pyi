from src.CxAdmin.api.cxItem import CxItem as CxItem
from src.CxAdmin.objects import CxQueue as CxQueue
from typing import Any

class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]: ...
    def get(self) -> Any: ...
