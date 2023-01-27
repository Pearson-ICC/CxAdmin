from datetime import datetime
from typing import Any
from CxAdmin.api.cxItem import CxItem


class CxStatistics(CxItem):
    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]:
        params: str = f"?start={between[0]}&end={between[1]}&limit=1000"
        responsesJsons: list[dict[str, Any]] = []
        response = self._httpClient.get(f"{self._path}/interactions{params}")
        responseJson = response.json()
        responseResults = responseJson["results"]
        responsesJsons.extend(responseResults)
        while len(responsesJsons) < responseJson["total"]:
            params = f"?start={between[0]}&end={between[1]}&limit=1000&offset={len(responsesJsons)}"
            response = self._httpClient.get(f"{self._path}/interactions{params}")
            responseJson = response.json()
            responseResults = responseJson["results"]
            responsesJsons.extend(responseResults)

        return responsesJsons

    def get(self) -> Any:
        statsJson: list[dict[str, Any]] = self._httpClient.get(
            f"{self._path}/statistics"
        ).json()["result"]
        return statsJson
