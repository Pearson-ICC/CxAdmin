from CxAdmin.api.cxItem import CxItem as CxItem
from typing import Any

class CxEnvironment(CxItem[Any]):
    def getTenant(self) -> Any: ...
    def getRegions(self) -> Any: ...
    def get(self) -> Any: ...