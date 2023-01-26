from src.CxAdmin.api.cxItem import CxItem as CxItem
from src.CxAdmin.objects import CxUser as CxUser
from typing import Any

class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]: ...
    def get(self) -> Any: ...
