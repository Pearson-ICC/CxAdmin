from typing import Any
from src.CxAdmin.api.cxItem import CxItem


class CxEnvironment(CxItem):
    def getTenant(self) -> Any:
        raise NotImplementedError()

    def getRegions(self) -> Any:
        raise NotImplementedError()

    def get(self) -> Any:
        return self._httpClient.get(self._path).json()
