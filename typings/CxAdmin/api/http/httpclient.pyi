from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from requests import Response as Response
from typing import Any

class HTTPClient(HTTPClientModel):
    def __init__(self, basePath: str, token: str) -> None: ...
    def get(self, path: str) -> Response: ...
    def post(self, path: str, data: Any) -> Response: ...
    @staticmethod
    def getToken(basePath: str, apiKey: str, apiSecret: str, tenantID: str) -> str: ...