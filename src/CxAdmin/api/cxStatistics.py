from datetime import datetime
from typing import Any, Generator
from CxAdmin.api.cxItem import CxItem


class CxStatistics(CxItem[dict[str, Any]]):
    def get(self) -> list[dict[str, Any]]:
        raise NotImplementedError()

    def getInteractions(
        self,
        between: tuple[datetime, datetime],
        verbose: bool = False,
    ) -> Generator[dict[str, Any], None, None]:
        betweenStr = [b.isoformat() for b in between]
        responsesJsons: list[dict[str, Any]] = []
        while True:
            params = f"?start={betweenStr[0]}&end={betweenStr[1]}&limit=1000&offset={len(responsesJsons)}"
            response = self._httpClient.get(f"{self._path}/interactions{params}")
            responseJson = response.json()
            if len(responsesJsons) >= responseJson["total"]:
                break
            if verbose:
                offset = responseJson["offset"]
                total = responseJson["total"]
                print(f"Fetched record {offset} of {total}")
            responseResults = responseJson["results"]
            for result in responseResults:
                yield result

    # def get(self) -> list[dict[str, Any]]:
    # statsJson: list[dict[str, Any]] = self._httpClient.get(
    #     f"{self._path}/statistics" # endpoint does not exist
    # ).json()["result"]
    # return statsJson

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
            "queue1Name",
            "queue1Time",
            "queue2Name",
            "queue2Time",
            "queue3Name",
            "queue3Time",
            "queue4Name",
            "queue4Time",
            "queue5Name",
            "queue5Time",
            "queue6Name",
            "queue6Time",
            "queue7Name",
            "queue7Time",
            "queue8Name",
            "queue8Time",
            "queue9Name",
            "queue9Time",
            "queue10Name",
            "queue10Time",
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
            for i, queue in enumerate(interaction.get("queues", []), start=1):
                data[f"queue{i}Name"] = queue["queueId"]
                data[f"queue{i}Time"] = queue["queueTime"]
            yield ",".join([str(data[heading]) for heading in headings])

    def getCalls(
        self, between: tuple[datetime, datetime]
    ) -> Generator[dict[str, Any], None, None]:
        interactions = self.getInteractions(between)
        # calls are interactions where the property `ivrAbandoned` either does not exist or is false
        for interaction in interactions:
            ivrAbandoned = interaction.get("ivrAbandoned")  # (False | None) | True
            if (ivrAbandoned is None) or (ivrAbandoned == False):
                yield interaction
