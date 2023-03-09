from typing import Any
from CxAdmin.jsonable import JSONSerializable

class CxQueue(JSONSerializable):
    tenantID: str
    name: str
    description: str
    updated: str
    updatedBy: str
    created: str
    createdBy: str
    active: str
    activeVersion: str
    id: str
    def __init__(
        self,
        tenantID: str,
        name: str,
        description: str,
        updated: str,
        updatedBy: str,
        created: str,
        createdBy: str,
        active: bool,
        activeVersion: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxQueue: ...
    def to_json(self) -> dict[str, Any]: ...
