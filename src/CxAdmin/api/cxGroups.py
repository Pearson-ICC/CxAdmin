from typing import Any
from src.CxAdmin.api.cxItem import CxItem
from src.CxAdmin.objects import CxGroup


class CxGroups(CxItem):
    def getGroups(self) -> list[CxGroup]:
        groupsJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        groups = [CxGroup.from_json(groupJson) for groupJson in groupsJson]
        return groups

    def get(self) -> Any:
        return self.getGroups()
