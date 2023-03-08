from CxAdmin.api.cxItem import CxItem as CxItem
from datetime import datetime
from typing import Any

class CxStatistics(CxItem[Any]):
    def getInteractions(
        self, between: tuple[datetime, datetime]
    ) -> list[dict[str, Any]]: ...
    def get(self) -> Any: ...
