import abc
from typing import Any


class HTTPClientModel:
    @abc.abstractmethod
    def __init__(self, basePath: str, token: str):
        ...

    @abc.abstractmethod
    def get(self, path: str, withResultJsonKey: bool = True) -> list[dict[str, Any]]:
        ...

    @abc.abstractmethod
    def post(
        self, path: str, data: Any, withResultJsonKey: bool = True
    ) -> dict[str, Any]:
        ...

    @staticmethod
    @abc.abstractmethod
    def getToken(basePath: str, apiKey: str, apiSecret: str, tenantID: str) -> str:
        ...
