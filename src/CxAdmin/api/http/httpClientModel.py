import abc
from typing import Any
from requests import Response


class HTTPClientModel:
    @abc.abstractmethod
    def __init__(self, basePath: str, token: str) -> None:
        ...

    @abc.abstractmethod
    def get(self, path: str) -> Response:
        ...

    @abc.abstractmethod
    def post(self, path: str, data: Any) -> Response:
        ...

    @staticmethod
    @abc.abstractmethod
    def getToken(basePath: str, apiKey: str, apiSecret: str, tenantID: str) -> str:
        ...
