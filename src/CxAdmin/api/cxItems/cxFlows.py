from typing import Any
from CxAdmin.api.cxItems.cxItem import CxItem


class CxFlows(CxItem):
    def getAllFlows(self) -> Any:
        raise NotImplementedError()

    def getFlow(self, flowId: str) -> Any:
        raise NotImplementedError()
