from typing import Any

class CxGroup(dict[str, Any]):
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
