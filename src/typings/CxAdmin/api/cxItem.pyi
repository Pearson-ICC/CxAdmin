import abc
from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from abc import abstractmethod
from typing import Any

class CxItem(metaclass=abc.ABCMeta):
    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    @abstractmethod
    def get(self) -> list[Any]: ...
