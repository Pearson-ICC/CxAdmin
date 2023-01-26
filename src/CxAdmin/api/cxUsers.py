from typing import Any
from src.CxAdmin.api import CxItem
from src.CxAdmin.objects import CxUser


class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]:
        usersJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        users = [CxUser.from_json(userJson) for userJson in usersJson]
        return users

    def get(self) -> Any:
        raise NotImplementedError()
