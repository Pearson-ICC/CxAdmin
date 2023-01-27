from CxAdmin.api.cxItem import CxItem as CxItem
from CxAdmin.objects.__cxUser import CxUser as CxUser
from typing import Any

class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]: ...
    def get(self) -> Any: ...
