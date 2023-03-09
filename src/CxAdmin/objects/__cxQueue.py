from typing import Any
from CxAdmin.jsonable import JSONSerializable


class CxQueue(JSONSerializable):
    """
    | Parameter | Type | Description |
    | --- | --- | --- |
    | tenantId | `UUID` | The unique identifier of the tenant with which the queue is associated. |
    | name | `string` | The name of the queue. |
    | description | `string` | The human-readable description of the queue. |
    | updated | `string` | The date and time (in UTC format) when the queue was last updated. |
    | updatedBy | `UUID` | The unique identifier of the user who last updated the queue. |
    | created | `string` | The date and time (in UTC format) when the queue was created. |
    | createdBy | `string` | The unique identifier of the user who created the queue. |
    | active | `string` | A flag indicating whether or not the queue is in use. |
    | activeVersion | `string` | The version of the queue that is in use. |
    | id | `UUID` | The ID of the queue |
    """

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
    ):
        self.tenantID = tenantID
        self.name = name
        self.description = description
        self.updated = updated
        self.updatedBy = updatedBy
        self.created = created
        self.createdBy = createdBy
        self.active = active
        self.activeVersion = activeVersion
        self.id = id

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxQueue":
        return CxQueue(
            tenantID=data["tenantId"],
            name=data["name"],
            description=data["description"],
            updated=data["updated"],
            updatedBy=data["updatedBy"],
            created=data["created"],
            createdBy=data["createdBy"],
            active=data["active"],
            activeVersion=data["activeVersion"],
            id=data["id"],
        )

    def __str__(self) -> str:
        return f"CxQueue({self.name}, {self.id})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_json(self) -> dict[str, Any]:
        return {
            "tenantID": self.tenantID,
            "name": self.name,
            "description": self.description,
            "updated": self.updated,
            "updatedBy": self.updatedBy,
            "created": self.created,
            "createdBy": self.createdBy,
            "active": self.active,
            "activeVersion": self.activeVersion,
            "id": self.id,
        }
