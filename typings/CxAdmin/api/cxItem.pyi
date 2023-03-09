import abc
from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from CxAdmin.jsonable import JSONSerializable
from abc import abstractmethod
from typing import TypeVar, Generic, Any, Union

A = TypeVar(
    "A",
    bound=Union[
        JSONSerializable,
        list[JSONSerializable],
        list[dict[str, Any]],
        dict[str, Any],
        str,
    ],
)

class CxItem(Generic[A], metaclass=abc.ABCMeta):
    _httpClient: HTTPClientModel
    _path: str

    def __init__(self, httpClient: HTTPClientModel, path: str) -> None: ...
    @abstractmethod
    def get(self) -> list[A]: ...
