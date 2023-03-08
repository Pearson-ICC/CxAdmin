from CxAdmin.api.http.httpClientModel import HTTPClientModel
from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class CxItem(Generic[T]):
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    @abstractmethod
    def get(self) -> list[T]:
        raise NotImplementedError()
