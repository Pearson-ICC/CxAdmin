from CxAdmin.api.http.httpClientModel import HTTPClientModel
from abc import abstractmethod
from typing import TypeVar, Generic, Any

class CxItem:
    _httpClient: HTTPClientModel
    _path: str

    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    @abstractmethod
    def get(self) -> list[Any]: ...

T = TypeVar("T", bound=CxItem)

class CxCollection(Generic[T]):
    @abstractmethod
    def get(self) -> list[T]: ...
    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
