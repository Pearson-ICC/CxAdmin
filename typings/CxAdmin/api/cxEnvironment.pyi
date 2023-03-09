from CxAdmin.api.cxItem import CxItem as CxItem
from typing import Any

class CxEnvironment(CxItem[dict[str, Any]]):
    def getTenant(self) -> dict[str, Any]: ...
    def getRegions(self) -> dict[str, Any]: ...
    def get(self) -> dict[str, Any]: ...
