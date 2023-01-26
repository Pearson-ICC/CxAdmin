from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects import CxGroup
from typing import Any

class CxGroups(CxItem):
    def getGroups(self) -> list[CxGroup]: ...
    def get(self) -> Any: ...
