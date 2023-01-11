from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxUser import CxUser


class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]:
        usersJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        users = [CxUser.from_json(userJson) for userJson in usersJson]
        return users
