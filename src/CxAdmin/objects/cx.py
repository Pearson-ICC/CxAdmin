from CxAdmin.api.cxLists import CxLists
from CxAdmin.api.cxQueues import CxQueues
from CxAdmin.api.cxStatistics import CxStatistics
from CxAdmin.api.cxEnvironment import CxEnvironment
from CxAdmin.api.cxFlows import CxFlows
from CxAdmin.api.cxUsers import CxUsers
from CxAdmin.api.cxItem import CxCollection

from CxAdmin.api.http.httpclient import HTTPClient
from CxAdmin.api.http.httpClientModel import HTTPClientModel

import json


class Cx:
    __BASE_URL: str
    __API_KEY: str
    __API_SECRET: str
    __TENANT_ID: str
    __TENANT_URL: str

    __httpClient: HTTPClientModel

    environment: CxCollection[CxEnvironment]
    flows: CxCollection[CxFlows]
    lists: CxCollection[CxLists]
    queues: CxCollection[CxQueues]
    statistics: CxCollection[CxStatistics]
    users: CxCollection[CxUsers]

    def __init__(self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str):
        self.__BASE_URL = baseURL  # type: ignore
        self.__API_KEY = apiKey  # type: ignore
        self.__API_SECRET = apiSecret  # type: ignore
        self.__TENANT_ID = tenantID  # type: ignore
        self.__TENANT_URL = f"{self.__BASE_URL}/v1/tenants/{self.__TENANT_ID}"  # type: ignore

        self.__httpClient = HTTPClient(
            basePath=self.__TENANT_URL,
            token=self.__getToken(),
        )

        self.environment = CxCollection(self.__httpClient, "")
        self.flows = CxCollection(self.__httpClient, "/flows")
        self.lists = CxCollection(self.__httpClient, "/lists")
        self.queues = CxCollection(self.__httpClient, "/queues")
        self.statistics = CxCollection(self.__httpClient, "")
        self.users = CxCollection(self.__httpClient, "/users")

    @staticmethod
    def fromConfigFile(configFilePath: str) -> "Cx":
        config: dict[str, str]
        with open(file=configFilePath, mode="r") as file:
            config = json.load(file)

        return Cx(
            baseURL=config["baseURL"],
            apiKey=config["apiKey"],
            apiSecret=config["apiSecret"],
            tenantID=config["tenantID"],
        )

    def __getToken(self) -> str:
        token = HTTPClient.getToken(
            self.__BASE_URL,
            self.__API_KEY,
            self.__API_SECRET,
            self.__TENANT_ID,
        )

        return token
