from datetime import datetime
from typing import Any
from CxAdmin.api.cxItem import CxItem


class CxStatistics(CxItem):
    def getRealtimeStatistics(self) -> Any:
        raise NotImplementedError()

    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]:
        params: str = f"?start={between[0]}&end={between[1]}&limit=1000"
        responsesJsons: list[dict[str, Any]] = []
        response = self._httpClient.get(f"{self._path}/interactions{params}")
        responseResults = response.json()["results"]["interactions"]
        responsesJsons.extend(responseResults)
        while len(responseResults) >= 1000:
            params = f"?start={between[0]}&end={between[1]}&limit=1000&offset={len(responsesJsons)}"
            response = self._httpClient.get(f"{self._path}/interactions{params}")
            responseResults = response.json()
            responsesJsons.extend(responseResults["results"])

        return responsesJsons
