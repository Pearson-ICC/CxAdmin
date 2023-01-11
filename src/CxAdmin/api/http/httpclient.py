from CxAdmin.api.http.httpClientModel import HTTPClientModel
from typing import Any, Optional
from requests import get, post, Response


class HTTPClient(HTTPClientModel):
    __basePath: str
    __token: str
    __headers: dict[str, Any]

    def __init__(self, basePath: str, token: str):
        self.__basePath = basePath
        self.__token = token
        self.__headers = {
            "Authorization": f"Token {self.__token}",
            "Content-Type": "application/json",
        }

    def get(self, path: str) -> Response:
        response = HTTPClient._get(
            path=self.__basePath + path,
            headers=self.__headers,
        )
        return response

    def post(self, path: str, data: Any) -> Response:
        response = HTTPClient._post(
            path=self.__basePath + path,
            headers=self.__headers,
            body=data,
        )
        return response

    @staticmethod
    def _get(path: str, headers: dict[str, Any]) -> Response:
        response = get(path, headers=headers)
        return response

    @staticmethod
    def _post(
        path: str,
        body: Optional[dict[str, Any]],
        headers: Optional[dict[str, Any]] = None,
    ) -> Response:
        response = post(url=path, json=body, headers=headers)
        return response

    @staticmethod
    def getToken(basePath: str, apiKey: str, apiSecret: str, tenantID: str) -> str:
        body = {
            "username": apiKey,
            "password": apiSecret,
            "tenantId": tenantID,
        }

        response = HTTPClient._post(
            path=f"{basePath}/v1/tokens",
            body=body,
        )

        token: str = response.json()["token"]
        return token
