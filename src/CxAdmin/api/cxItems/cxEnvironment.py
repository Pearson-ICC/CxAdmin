from typing import Any
from CxAdmin.api.cxItems.cxItem import CxItem


class CxEnvironment(CxItem):
    def getTenant(self) -> Any:
        raise NotImplementedError()

    def getRegions(self) -> Any:
        raise NotImplementedError()
