from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxQueue import CxQueue as CxQueue

class CxQueues(CxItem):
    def getQueues(self) -> list[CxQueue]: ...
