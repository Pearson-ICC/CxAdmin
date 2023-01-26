from src.CxAdmin.api.cxItem import CxItem as CxItem
from src.CxAdmin.objects import CxGroup as CxGroup
from typing import Any

class CxGroups(CxItem):
    def getGroups(self) -> list[CxGroup]: ...
    def get(self) -> Any: ...
