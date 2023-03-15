from CxAdmin.api.cxItem import CxItem as CxItem
from datetime import datetime
from typing import Any, Generator

class CxStatistics(CxItem[Any]):
    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]: ...
    def get(self) -> list[dict[str, Any]]: ...
    @staticmethod
    def convertInteractionsToCSV(
        interactions: list[dict[str, Any]]
    ) -> Generator[str, None, None]: ...
