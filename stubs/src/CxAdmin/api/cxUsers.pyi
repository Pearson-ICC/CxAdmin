from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects import CxUser
from typing import Any

class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]: ...
    def get(self) -> Any: ...
