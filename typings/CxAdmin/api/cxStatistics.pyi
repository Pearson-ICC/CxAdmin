from CxAdmin.api.cxItem import CxItem
from datetime import datetime
from typing import Any

class CxStatistics(CxItem):
    def getInteractions(self, between: tuple[datetime, datetime]) -> list[dict[str, Any]]: ...
