from typing import Any
from src.CxAdmin.api import CxItem


class CxFlows(CxItem):
    def getAllFlows(self) -> Any:
        raise NotImplementedError()

    def getFlow(self, flowId: str) -> Any:
        raise NotImplementedError()

    def get(self) -> Any:
        raise NotImplementedError()
