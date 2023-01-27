from typing import Any
from CxAdmin.api.cxItem import CxItem


class CxEnvironment(CxItem):
    def getTenant(self) -> Any:
        return self._httpClient.get(self._path).json()

    def getRegions(self) -> Any:
        return self._httpClient.get(f"{self._path}/regions").json()

    def get(self) -> Any:
        return self.getTenant()
