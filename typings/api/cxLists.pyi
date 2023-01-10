"""
This type stub file was generated by pyright.
"""

from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxList import CxList

class CxLists(CxItem):
    def getAllLists(self) -> list[CxList]: ...
    def getList(self, listId: str) -> CxList: ...
    def uploadList(self, list: CxList) -> dict[str, Any]: ...
    def uploadRoutingLists(self, lists: list[CxList]) -> None: ...
    def getListCSV(self, listId: str) -> Any: ...