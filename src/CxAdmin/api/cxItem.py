import abc
from CxAdmin.api.http.httpClientModel import HTTPClientModel
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
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    @abstractmethod
    def get(self) -> list[A]:
        raise NotImplementedError()
