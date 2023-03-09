from typing import Any
from CxAdmin.csvable import CSVAble
from CxAdmin.jsonable import JSONSerializable

class CxListType(JSONSerializable):
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
    def to_json(self) -> dict[str, Any]: ...

class CxList(CSVAble, JSONSerializable):
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
    def to_json(self) -> dict[str, Any]: ...
