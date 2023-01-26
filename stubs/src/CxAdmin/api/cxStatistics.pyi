from datetime import datetime
from src.CxAdmin.api.cxItem import CxItem as CxItem
from typing import Any

class CxStatistics(CxItem):
    def getInteractions(self, between: tuple[datetime, datetime]) -> list[dict[str, Any]]: ...
    def get(self) -> Any: ...
