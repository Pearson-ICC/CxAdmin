from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from abc import abstractmethod
from typing import Any, TypeVar, Generic

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
