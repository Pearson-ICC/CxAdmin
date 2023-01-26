from src.CxAdmin.api import CxEnvironment as CxEnvironment, CxFlows as CxFlows, CxGroups as CxGroups, CxLists as CxLists, CxQueues as CxQueues, CxStatistics as CxStatistics, CxUsers as CxUsers
from src.CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from src.CxAdmin.api.http.httpclient import HTTPClient as HTTPClient

class Cx:
    environment: CxEnvironment
    flows: CxFlows
    lists: CxLists
    queues: CxQueues
    statistics: CxStatistics
    users: CxUsers
    groups: CxGroups
    def __init__(self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str) -> None: ...
    @staticmethod
    def fromConfigFile(configFilePath: str) -> Cx: ...
