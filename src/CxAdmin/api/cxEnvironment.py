from typing import Any
from api.cxItem import CxItem


class CxEnvironment(CxItem):
    def getTenant(self) -> Any:
        raise NotImplementedError()

    def getRegions(self) -> Any:
        raise NotImplementedError()
