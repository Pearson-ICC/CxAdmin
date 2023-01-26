from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from abc import abstractmethod
from typing import Any, Protocol

class CxItem(Protocol):
    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    @abstractmethod
    def get(self) -> list[Any]: ...
