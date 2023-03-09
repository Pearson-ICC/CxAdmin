from CxAdmin.api.cxItem import CxItem
from CxAdmin.api.http.httpClientModel import HTTPClientModel
from CxAdmin.objects.__cxBusinessHoursItem import CxBusinessHoursItem

class CxHours(CxItem[CxBusinessHoursItem]):
    _httpClient: HTTPClientModel
    _path: str

    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    def getHours(self) -> list[CxBusinessHoursItem]: ...
    def get(self) -> list[CxBusinessHoursItem]: ...
