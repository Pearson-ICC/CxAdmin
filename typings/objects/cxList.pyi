from typing import Any

class CxListType:
    def __init__(
        self,
        tenantID: str,
        description: str,
        createdBy: str,
        updated: str,
        name: str,
        fields: str,
        created: str,
        updatedBy: str,
        active: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxListType": ...

class CxList:
    def __init__(
        self,
        tenantId: str,
        listType: CxListType,
        createdBy: str,
        listTypeID: str,
        updated: str,
        name: str,
        created: str,
        updatedBy: str,
        active: str,
        id: str,
        shared: str,
        items: list[dict[str, Any]],
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxList": ...
    def constructDataCSV(self) -> str: ...
