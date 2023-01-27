from datetime import datetime
from CxAdmin.api.cxItem import CxItem
from typing import Any

class CxStatistics(CxItem):
    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]: ...
    def get(self) -> Any: ...
