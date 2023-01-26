from _typeshed import Incomplete
from typing import Any

class CxListType:
    tenantID: Incomplete
    description: Incomplete
    createdBy: Incomplete
    updated: Incomplete
    name: Incomplete
    fields: Incomplete
    created: Incomplete
    updatedBy: Incomplete
    active: Incomplete
    id: Incomplete
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

class CxList:
    tenantId: Incomplete
    listType: Incomplete
    createdBy: Incomplete
    listTypeID: Incomplete
    updated: Incomplete
    name: Incomplete
    created: Incomplete
    updatedBy: Incomplete
    active: Incomplete
    id: Incomplete
    shared: Incomplete
    items: Incomplete
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
    def from_json(data: dict[str, Any]) -> CxList: ...
    def constructDataCSV(self, headers: bool = ...) -> str: ...
