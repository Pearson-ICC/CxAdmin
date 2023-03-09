from CxAdmin.api.cxEnvironment import CxEnvironment as CxEnvironment
from CxAdmin.api.cxFlows import CxFlows as CxFlows
from CxAdmin.api.cxGroups import CxGroups as CxGroups
from CxAdmin.api.cxLists import CxLists as CxLists
from CxAdmin.api.cxQueues import CxQueues as CxQueues
from CxAdmin.api.cxStatistics import CxStatistics as CxStatistics
from CxAdmin.api.cxUsers import CxUsers as CxUsers
from CxAdmin.api.cxHours import CxHours
from CxAdmin.api.cxItem import CxItem

from CxAdmin.api.http.httpClientModel import HTTPClientModel as HTTPClientModel
from CxAdmin.api.http.httpclient import HTTPClient as HTTPClient

from CxAdmin.jsonable import JSONSerializable

from typing import Any, Union

class Cx:
    environment: CxEnvironment
    flows: CxFlows
    lists: CxLists
    queues: CxQueues
    users: CxUsers
    groups: CxGroups
    hours: CxHours
    statistics: CxStatistics

    items: list[Union[CxItem[JSONSerializable], CxItem[dict[str, Any]]]]

    def __init__(
        self, baseURL: str, apiKey: str, apiSecret: str, tenantID: str
    ) -> None: ...
    @staticmethod
    def fromConfigFile(configFilePath: str) -> Cx: ...
