from CxAdmin.api.cxEnvironment import CxEnvironment as CxEnvironment
from CxAdmin.api.cxFlows import CxFlows as CxFlows
from CxAdmin.api.cxLists import CxLists as CxLists
from CxAdmin.api.cxQueues import CxQueues as CxQueues
from CxAdmin.api.cxStatistics import CxStatistics as CxStatistics
from CxAdmin.api.cxUsers import CxUsers as CxUsers
from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel

class Cx:
    lists: CxLists
    queues: CxQueues
    statistics: CxStatistics
    environment: CxEnvironment
    flows: CxFlows
    users: CxUsers
    def __init__(self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str) -> None: ...
    @staticmethod
    def fromConfigFile(configFilePath: str) -> Cx: ...
