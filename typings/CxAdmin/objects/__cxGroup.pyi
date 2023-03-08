from _typeshed import Incomplete
from typing import Any

class CxGroup(dict[str, Any]):
    tenantId: Incomplete
    name: Incomplete
    owner: Incomplete
    status: Incomplete
    description: Incomplete
    created: Incomplete
    createdBy: Incomplete
    updated: Incomplete
    updatedBy: Incomplete
    id: Incomplete
    def __init__(self, tenantId: str, name: str, owner: str, status: bool, description: str, created: str, createdBy: str, updated: str, updatedBy: str, id: str) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxGroup: ...
