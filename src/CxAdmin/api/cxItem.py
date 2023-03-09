import abc
from CxAdmin.api.http.httpClientModel import HTTPClientModel
from CxAdmin.jsonable import JSONSerializable
from abc import abstractmethod
from typing import TypeVar, Generic, Any, Union

A = TypeVar(
    "A",
    bound=Union[
        list[JSONSerializable],
        JSONSerializable,
        list[dict[str, Any]],
        dict[str, Any],
        str,
    ],
    covariant=True,  # this took a while to bugfix…
)


class CxItem(Generic[A], metaclass=abc.ABCMeta):
    _httpClient: HTTPClientModel
    _path: str = ""

    def __init__(self, httpClient: HTTPClientModel, path: str):
        self._httpClient = httpClient
        self._path = path

    @abstractmethod
    def get(self) -> Union[A, list[A]]:
        raise NotImplementedError()
