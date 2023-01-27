from typing import Any
from CxAdmin.api.cxItem import CxItem


class CxFlows(CxItem):
    def getFlows(self) -> list[dict[str, Any]]:
        flowsJson: list[dict[str, Any]] = self._httpClient.get(self._path).json()[
            "result"
        ]
        # flows = [CxFlow.from_json(flowJson) for flowJson in flowsJson]
        # return flows
        return flowsJson

    def getFlow(self, flowId: str) -> Any:
        raise NotImplementedError()

    def get(self) -> Any:
        return self.getFlows()
