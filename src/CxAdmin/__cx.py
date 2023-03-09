from CxAdmin.api.cxLists import CxLists
from CxAdmin.api.cxQueues import CxQueues
from CxAdmin.api.cxStatistics import CxStatistics
from CxAdmin.api.cxEnvironment import CxEnvironment
from CxAdmin.api.cxFlows import CxFlows
from CxAdmin.api.cxUsers import CxUsers
from CxAdmin.api.cxGroups import CxGroups
from CxAdmin.api.cxHours import CxHours
from CxAdmin.api.cxItem import CxItem

from CxAdmin.api.http.httpclient import HTTPClient
from CxAdmin.api.http.httpClientModel import HTTPClientModel

from CxAdmin.jsonable import JSONSerializable

import json
from typing import Union, Any


class Cx:
    __base_url: str
    __api_key: str
    __api_secret: str
    __tenant_id: str
    __tenant_url: str

    __httpClient: HTTPClientModel

    environment: CxEnvironment
    flows: CxFlows
    lists: CxLists
    queues: CxQueues
    users: CxUsers
    groups: CxGroups
    hours: CxHours

    statistics: CxStatistics

    items: list[
        Union[
            CxItem[JSONSerializable],
            CxItem[dict[str, Any]],
        ],
    ]

    def __init__(self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str):
        self.__base_url = baseURL
        self.__api_key = apiKey
        self.__api_secret = apiSecret
        self.__tenant_id = tenantID
        self.__tenant_url = f"{self.__base_url}/v1/tenants/{self.__tenant_id}"

        self.__httpClient = HTTPClient(
            basePath=self.__tenant_url,
            token=self.__getToken(),
        )

        self.environment = CxEnvironment(self.__httpClient, "")
        self.flows = CxFlows(self.__httpClient, "/flows")
        self.lists = CxLists(self.__httpClient, "/lists")
        self.queues = CxQueues(self.__httpClient, "/queues")
        self.users = CxUsers(self.__httpClient, "/users")
        self.groups = CxGroups(self.__httpClient, "/groups")
        self.hours = CxHours(self.__httpClient, "/business-hours")

        self.statistics = CxStatistics(self.__httpClient, "")

        self.items = [
            self.environment,
            self.flows,
            self.lists,
            self.queues,
            self.users,
            self.groups,
            self.hours,
        ]

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
            self.__base_url,
            self.__api_key,
            self.__api_secret,
            self.__tenant_id,
        )

        return token
