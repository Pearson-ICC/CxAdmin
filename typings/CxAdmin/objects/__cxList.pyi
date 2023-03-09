from typing import Any
from CxAdmin.csvable import CSVAble

class CxListType:
    tenantID: str
    description: str
    createdBy: str
    updated: str
    name: str
    fields: str
    created: str
    updatedBy: str
    active: str
    id: str
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
    def from_json(data: dict[str, Any]) -> CxListType: ...

class CxList(CSVAble):
    tenantId: str
    listType: CxListType
    createdBy: str
    listTypeID: str
    updated: str
    name: str
    created: str
    updatedBy: str
    active: str
    id: str
    shared: str
    listItems: list[dict[str, Any]]

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
        listItems: list[dict[str, Any]],
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxList: ...
    def toCSV(self, headers: bool = ...) -> str: ...
    def __json__(self) -> dict[str, Any]: ...
