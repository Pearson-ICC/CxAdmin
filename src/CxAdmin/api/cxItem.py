from CxAdmin.api.http.httpClientModel import HTTPClientModel
from abc import abstractmethod
from typing import Protocol, TypeVar, Generic, Any


class CxItem(Protocol):
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    @abstractmethod
    def get(self) -> list[Any]:
        raise NotImplementedError()


T = TypeVar("T", bound=CxItem)


class CxCollection(Generic[T]):
    @abstractmethod
    def get(self) -> list[T]:
        pass

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path
