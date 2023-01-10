from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.objects.cxList import CxList


class CxLists(CxItem):
    @staticmethod
    def __split_csv(every: int, csv: str) -> list[str]:
        """Helper function to split a csv into chunks of a given size."""
        lines = csv.splitlines()
        # get header row
        header = lines[0]
        # return ["\n".join(lines[i : i + every]) for i in range(0, len(lines), every)]
        return [
            (header + "\n" + "\n".join(lines[i : i + every]))
            for i in range(1, len(lines), every)
        ]

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
            for i, csv_splitted in enumerate(self.__split_csv(1000, csv)):
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
