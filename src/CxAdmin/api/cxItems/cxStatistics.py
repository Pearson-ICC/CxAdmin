from typing import Any
from CxAdmin.api.cxItems.cxItem import CxItem


class CxStatistics(CxItem):
    def getRealtimeStatistics(self) -> Any:
        raise NotImplementedError()
