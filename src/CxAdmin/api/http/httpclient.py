from CxAdmin.api.http.httpClientModel import HTTPClientModel
from typing import Any, Optional
from requests import get, post


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

    def get(self, path: str, withResultJsonKey: bool = True) -> list[dict[str, Any]]:
        if withResultJsonKey == False:
            response = HTTPClient._get(
                path=self.__basePath + path,
                headers=self.__headers,
            )
            return response
        else:
            response = HTTPClient._get_json(
                path=self.__basePath + path,
                headers=self.__headers,
            )
            return response["result"]

    def post(
        self, path: str, data: Any, withResultJsonKey: bool = True
    ) -> dict[str, Any]:
        response = HTTPClient._post(
            path=self.__basePath + path,
            headers=self.__headers,
            body=data,
        )
        if withResultJsonKey:
            return response["result"]
        else:
            return response.text  # type: ignore

    @staticmethod
    def _get(path: str, headers: dict[str, Any]) -> Any:
        response = get(path, headers=headers)
        return response.text

    @staticmethod
    def _get_json(path: str, headers: dict[str, Any]) -> dict[str, Any]:
        response = get(url=path, headers=headers)
        return response.json()

    @staticmethod
    def _post(
        path: str,
        body: Optional[dict[str, Any]],
        headers: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        response = post(url=path, json=body, headers=headers)
        return response.json()

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

        token: str = response["token"]
        return token
