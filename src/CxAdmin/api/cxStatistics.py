from datetime import datetime
from typing import Any, Generator
from CxAdmin.api.cxItem import CxItem
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests import JSONDecodeError
import time


class CxStatistics(CxItem[dict[str, Any]]):
    def get(self) -> list[dict[str, Any]]:
        raise NotImplementedError()

    def getInteractions(
        self,
        between: tuple[datetime, datetime],
        verbose: bool = False,
    ) -> list[dict[str, Any]]:
        allCalls: list[dict[str, Any]] = []
        # check dates are in the correct order
        if between[0] > between[1]:
            raise ValueError("Dates must be in chronological order")
        betweenStr = [b.isoformat() for b in between]
        offset = 0
        total = 1
        while offset < total:
            responseJson: dict[str, Any] | None = None
            params = (
                f"?start={betweenStr[0]}&end={betweenStr[1]}&limit=1000&offset={offset}"
            )
            retry = True
            while retry:
                response = self._httpClient.get(f"{self._path}/interactions{params}")

                try:
                    responseJson = response.json()
                except JSONDecodeError:
                    if verbose:
                        print(f"Error {response.status_code}: {response.reason}")
                    if response.status_code == 503 or response.status_code == 504:
                        if verbose:
                            print(f"Retrying record offset {response.url[-4:]}...")
                        time.sleep(1)
                        retry = True
                    else:
                        retry = False
                else:
                    retry = False

            if responseJson is None:
                if verbose:
                    print(f"Failed to fetch {offset}")
                continue

            offset = responseJson["offset"]
            total = responseJson["total"]

            if verbose:
                print(f"Fetched record {offset} of {total}")
            responseResults = responseJson["results"]
            if responseResults is None:
                break
            offset += len(responseResults)
            allCalls.extend(responseResults)
            if offset >= total:
                break

        return allCalls

    def getInteractionsInParallel(
        self,
        between: tuple[datetime, datetime],
        verbose: bool = False,
        numThreads: int | None = 64,
    ) -> list[dict[str, Any]]:
        # check dates are in the correct order
        if between[0] > between[1]:
            raise ValueError("Dates must be in chronological order")
        betweenStr = [b.isoformat() for b in between]
        offset = 0
        params = f"?start={betweenStr[0]}&end={betweenStr[1]}&limit=0&offset={offset}"
        total = self._httpClient.get(f"{self._path}/interactions{params}").json()[
            "total"
        ]
        allInteractions: list[dict[str, Any]] = []

        with ThreadPoolExecutor(numThreads) as executor:
            futures = []
            if verbose:
                print(f"Mapping request executors across {numThreads} threads…")
            while offset < total:
                if verbose:
                    print(f"Mapping request {offset} of {total}…")
                params = f"?start={betweenStr[0]}&end={betweenStr[1]}&limit=1000&offset={offset}"
                futures.append(
                    executor.submit(
                        self._httpClient.get, f"{self._path}/interactions{params}"
                    )
                )
                offset += 1000

            if verbose:
                print("Waiting for responses…")

            for future in as_completed(futures):
                responseJson: dict[str, Any] | None = None
                retry = True
                while retry:
                    try:
                        responseJson = future.result().json()
                    except JSONDecodeError as e:
                        statusCode = future.result().status_code
                        if verbose:
                            print(f"Error {statusCode}: {future.result().reason}")
                        if statusCode == 503 or statusCode == 504:
                            if verbose:
                                print(
                                    f"Retrying record offset {future.result().url[-4:]}..."
                                )
                            time.sleep(5)
                            retry = True
                        else:
                            retry = False
                    else:
                        retry = False

                responseResults = responseJson["results"]
                offset = responseJson["offset"]
                total = responseJson["total"]
                if verbose:
                    print(f"Fetched record {offset} of {total}")
                if responseResults is None:
                    break
                allInteractions.extend(responseResults)

        print(f"Fetched {len(allInteractions)} interactions")
        return allInteractions

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
