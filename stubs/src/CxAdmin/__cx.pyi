from CxAdmin.api import (
    CxEnvironment,
    CxFlows,
    CxGroups,
    CxLists,
    CxQueues,
    CxStatistics,
    CxUsers,
)
from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel

class Cx:
    environment: CxEnvironment
    flows: CxFlows
    lists: CxLists
    queues: CxQueues
    statistics: CxStatistics
    users: CxUsers
    groups: CxGroups
    def __init__(
        self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str
    ) -> None: ...
    @staticmethod
    def fromConfigFile(configFilePath: str) -> Cx: ...
