from typing import Any
from CxAdmin.api.cxItems.cxItem import CxItem
from CxAdmin.objects.cxList import CxList
from CxAdmin.api.cxItems.split_csvs import split_csv


class CxLists(CxItem):
    def getAllLists(self) -> list[CxList]:
        listsJson: list[dict[str, str]] = self._httpClient.get(self._path)
        lists = [CxList.from_json(thisListJson) for thisListJson in listsJson]
        return lists

    def getList(self, listId: str) -> CxList:
        listJson: dict[str, Any] = self._httpClient.get(f"{self._path}/{listId}")  # type: ignore
        listItem = CxList.from_json(listJson)
        return listItem

    def uploadList(self, list: CxList) -> dict[str, Any]:
        listJson: dict[str, Any] = self._httpClient.post(
            f"{self._path}/{list.id}/upload",
            list.constructDataCSV(),
            withResultJsonKey=False,
        )
        return listJson

    def uploadRoutingLists(self, lists: list[CxList]) -> None:
        # leftover from internal project
        for routingList in lists:
            # You can sort the list items here with `routingList.items.sort()`
            csv = routingList.constructDataCSV()

            file = open(f"output/{routingList.name}.csv", "w")
            file.write(csv)
            file.close()

            # split csv into 1000 line chunks as CxEngage only lets you upload 1000 at a time
            for i, csv_splitted in enumerate(split_csv(1000, csv)):
                print(len(csv_splitted.splitlines()))
                file = open(f"output/{routingList.name}_split_{i}.csv", "w")
                file.write(csv_splitted)
                file.close()
                # upload the csv
                self._httpClient.post(
                    f"{self._path}/{routingList.id}/upload",
                    csv_splitted,
                    withResultJsonKey=False,
                )

    def getListCSV(self, listId: str) -> Any:
        return self._httpClient.get(
            f"{self._path}/{listId}/download/list-items.csv",
            withResultJsonKey=False,
        )
