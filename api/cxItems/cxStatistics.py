from typing import Any
from api.cxItems.cxItem import CxItem


class CxStatistics(CxItem):
    def getRealtimeStatistics(self) -> Any:
        raise NotImplementedError()
