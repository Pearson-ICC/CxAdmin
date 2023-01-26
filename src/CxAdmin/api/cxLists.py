from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.__cxList import CxList
import json


class CxLists(CxItem):
    def get(self) -> list[CxList]:
        listsJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        lists = [CxList.from_json(thisListJson) for thisListJson in listsJson]
        return lists

    def getList(self, listId: str) -> CxList:
        listJson: str = self._httpClient.get(f"{self._path}/{listId}").json()
        listItem = CxList.from_json(json.loads(listJson)["result"])
        return listItem

    def uploadListCSV(self, id: str, csv: str) -> dict[str, Any]:
        raise NotImplementedError(
            r"Not yet implemented. See https://api-docs.cxengage.net/Rest/Default.htm#Lists/bulk_Import_Lists.htm%3FTocPath%3DConfiguration%7CManaging%2520Lists%7CLists%7C_____6"
        )
        listJson: dict[str, Any] = self._httpClient.post(
            f"{self._path}/{id}/upload", csv
        )
        return listJson

    def uploadList(self, list: CxList) -> dict[str, Any]:
        return self.uploadListCSV(
            list.id,
            list.constructDataCSV(),
        )

    def getListCSV(self, listId: str) -> Any:
        return self._httpClient.get(f"{self._path}/{listId}/download/list-items.csv")
