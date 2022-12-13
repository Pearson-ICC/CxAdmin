from api.cxItems.cxLists import CxLists
from api.cxItems.cxQueues import CxQueues
from api.cxItems.cxStatistics import CxStatistics
from api.cxItems.cxEnvironment import CxEnvironment
from api.cxItems.cxFlows import CxFlows

from api.httpclient import HTTPClient
from api.httpClientModel import HTTPClientModel

import json


class Cx:
    __BASE_URL: str
    __API_KEY: str
    __API_SECRET: str
    __TENANT_ID: str
    __TENANT_URL: str

    __httpClient: HTTPClientModel

    lists: CxLists
    queues: CxQueues
    statistics: CxStatistics
    environment: CxEnvironment
    flows: CxFlows

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

        self.lists = CxLists(self.__httpClient, "/lists")
        self.queues = CxQueues(self.__httpClient, "/queues")
        self.statistics = CxStatistics(self.__httpClient, "/realtime-statistics")
        self.environment = CxEnvironment(self.__httpClient, "")
        self.flows = CxFlows(self.__httpClient, "/flows")

    @staticmethod
    def fromConfigFile(configFilePath: str) -> "Cx":
        config: dict[str, str]
        with open(configFilePath, "r") as file:
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
