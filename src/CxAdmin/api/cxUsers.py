import json
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxUser import CxUser


class CxUsers(CxItem):
    def getAllUsers(self) -> list[CxUser]:
        usersJson: str = self._httpClient.get(self._path)
        users = [
            CxUser.from_json(json.loads(userJson)["result"]) for userJson in usersJson
        ]
        return users
