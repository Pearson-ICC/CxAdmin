from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxUser import CxUser as CxUser

class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]: ...
