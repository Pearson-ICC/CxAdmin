from datetime import datetime
from typing import Any, Generator
from CxAdmin.api.cxItem import CxItem


class CxStatistics(CxItem[dict[str, Any]]):
    def getInteractions(
        self,
        between: tuple[datetime, datetime],
        verbose: bool = False,
    ) -> list[dict[str, Any]]:
        params: str = f"?start={between[0]}&end={between[1]}&limit=1000"
        responsesJsons: list[dict[str, Any]] = []
        response = self._httpClient.get(f"{self._path}/interactions{params}")
        responseJson = response.json()
        responseResults = responseJson["results"]
        responsesJsons.extend(responseResults)
        while len(responsesJsons) < responseJson["total"]:
            params = f"?start={between[0]}&end={between[1]}&limit=1000&offset={len(responsesJsons)}"
            response = self._httpClient.get(f"{self._path}/interactions{params}")
            responseJson = response.json()
            if verbose:
                offset = responseJson["offset"]
                total = responseJson["total"]
                print(f"Fetched record {offset} of {total}")
            responseResults = responseJson["results"]
            responsesJsons.extend(responseResults)

        return responsesJsons

    def get(self) -> list[dict[str, Any]]:
        statsJson: list[dict[str, Any]] = self._httpClient.get(
            f"{self._path}/statistics"
        ).json()["result"]
        return statsJson

    @staticmethod
    def convertInteractionsToCSV(
        interactions: list[dict[str, Any]]
    ) -> Generator[str, None, None]:
        headings: list[str] = [
            "monitors",  # float
            "customerHoldTime",  # float
            "ivrAbandoned",  # bool
            "customerHoldAbandoned",  # bool
            "customerHolds",  # int
            # "hooks",  # list[dict[str, Any]] # ignore
            "interactionTime",  # float
            "audioRecording",  # bool
            "customerConversationTime",  # float
            "tenantId",  # str
            # "customerTalkTimes",  # list[dict[str, Any]] # ignore
            "contactPoint",  # str
            # "queues",  # list[dict[str, Any]] # ignore
            "artifactsSummary",  # str
            "channelType",  # str
            # "interactionAttributes",  # list[dict[str, Any]] # ignore
            "direction",  # str
            "notes",  # list[dict[str, Any]] # ignore
            "flagged",  # bool
            "updated",  # str iso8601
            # "customerHoldTimes",  # list[dict[str, Any]] # ignore
            "endTimestamp",  # str iso8601
            "ivrAbandonTime",  # float
            # "segments",  # list[dict[str, Any]] # ignore
            "customerTransfers",  # int
            "flagTimestamp",  # str iso8601
            "startTimestamp",  # str iso8601
            "flowName",  # str
            "customerTalkTime",  # float
            "customerAbandonTime",  # float
            "flowId",  # str
            "ivrTime",  # float
            "customer",  # str
            "flagType",  # str
            # "agents",  # list[dict[str, Any]] # ignore
            "interactionId",  # str
        ]
        """
            "queueXName",  # data["queues"][X]["queueId"] # str
            "queueXTime",  # data["queues"][X]["queueTime"] # float
        """

        yield ",".join(headings)

        for interaction in interactions:
            data: dict[str, str | float | bool | int] = dict()
            for heading in headings:
                data[heading] = interaction.get(heading, "")
            for i, queue in enumerate(interaction.get("queues", [])):
                data[f"queue{i}Name"] = queue["queueId"]
                data[f"queue{i}Time"] = queue["queueTime"]
            yield ",".join([str(data[heading]) for heading in headings])
