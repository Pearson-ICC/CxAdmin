from CxAdmin.api.cxItem import CxItem as CxItem
from datetime import datetime
from typing import Any, Generator

class CxStatistics(CxItem[Any]):
    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]: ...
    def get(self) -> Generator[dict[str, Any], None, None]: ...
    @staticmethod
    def convertInteractionsToCSV(
        interactions: list[dict[str, Any]]
    ) -> Generator[str, None, None]: ...
    def getCalls(
        self, between: tuple[datetime, datetime]
    ) -> Generator[dict[str, Any], None, None]: ...
