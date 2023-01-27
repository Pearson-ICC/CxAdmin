from _typeshed import Incomplete
from typing import Any

class CxQueue:
    tenantID: Incomplete
    name: Incomplete
    description: Incomplete
    updated: Incomplete
    updatedBy: Incomplete
    created: Incomplete
    createdBy: Incomplete
    active: Incomplete
    activeVersion: Incomplete
    id: Incomplete
    def __init__(self, tenantID: str, name: str, description: str, updated: str, updatedBy: str, created: str, createdBy: str, active: str, activeVersion: str, id: str) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> CxQueue: ...
