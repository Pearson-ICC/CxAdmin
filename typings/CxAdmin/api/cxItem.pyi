import abc
from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from CxAdmin.jsonable import JSONSerializable
from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T", bound=JSONSerializable)

class CxItem(Generic[T], metaclass=abc.ABCMeta):
    _httpClient: HTTPClientModel
    _path: str

    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    @abstractmethod
    def get(self) -> list[T]: ...
