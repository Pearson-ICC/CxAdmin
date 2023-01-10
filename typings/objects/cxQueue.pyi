from typing import Any

class CxQueue:
    def __init__(
        self,
        tenantID: str,
        name: str,
        description: str,
        updated: str,
        updatedBy: str,
        created: str,
        createdBy: str,
        active: str,
        activeVersion: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxQueue": ...
    def __str__(self) -> str: ...
