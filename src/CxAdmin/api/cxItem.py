from CxAdmin.api.http.httpClientModel import HTTPClientModel


class CxItem:
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path
