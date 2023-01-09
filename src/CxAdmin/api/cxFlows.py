from typing import Any
from api.cxItem import CxItem


class CxFlows(CxItem):
    def getAllFlows(self) -> Any:
        raise NotImplementedError()

    def getFlow(self, flowId: str) -> Any:
        raise NotImplementedError()
