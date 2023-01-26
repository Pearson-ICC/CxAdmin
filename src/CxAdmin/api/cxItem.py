from CxAdmin.api.http.httpClientModel import HTTPClientModel
from abc import abstractmethod
from typing import Any


class CxItem:
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    @abstractmethod
    def get(self) -> list[Any]:
        raise NotImplementedError()
