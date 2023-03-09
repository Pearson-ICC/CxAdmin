from typing import Any
from CxAdmin.jsonable import JSONSerializable

class CxGroup(JSONSerializable):
    tenantId: str
    name: str
    owner: str
    status: str
    description: str
    created: str
    createdBy: str
    updated: str
    updatedBy: str
    id: str
    def __init__(
        self,
        tenantId: str,
        name: str,
        owner: str,
        status: bool,
        description: str,
        created: str,
        createdBy: str,
        updated: str,
        updatedBy: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxGroup: ...
    def to_json(self) -> dict[str, Any]: ...
