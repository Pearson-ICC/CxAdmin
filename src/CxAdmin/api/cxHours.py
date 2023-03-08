from typing import Any
from CxAdmin.api.cxItem import CxItem
from CxAdmin.api.http.httpClientModel import HTTPClientModel
from CxAdmin.objects.__cxBusinessHoursItem import CxBusinessHoursItem


class CxHours(CxItem[CxBusinessHoursItem]):
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str) -> None:
        self._httpClient = httpClient
        self._path = path

    def getHours(self) -> list[CxBusinessHoursItem]:
        hoursJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        hours = [CxBusinessHoursItem.from_json(thisJson) for thisJson in hoursJson]
        return hours

    def get(self) -> list[CxBusinessHoursItem]:
        return self.getHours()
