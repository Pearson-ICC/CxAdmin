from typing import Any


class CxGroup:
    """
    A group includes the following parameters:

    | Parameter | Type | Description |
    | --- | --- | --- |
    | tenantId | `UUID` | The tenant's unique identifier. |
    | name | `string` | The name of the group. |
    | owner | `UUID` | The unique identifier of the user who owns the group. |
    | status | `boolean` | Whether or not the group is enabled. |
    | description | `string` | A description of the group. |
    | created | `string` | The date and time, in UTC format, when the group was created. |
    | createdBy | `UUID` | The unique identifier of the user who created the group. |
    | updated | `string` | The date and time, in UTC format, when the group was last modified. |
    | updatedBy | `UUID` | The unique identifier of the user who last updated the group. |
    | id | `UUID` | The group's unique identifier. |
    """

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
    ):
        self.tenantId = tenantId
        self.name = name
        self.owner = owner
        self.status = status
        self.description = description
        self.created = created
        self.createdBy = createdBy
        self.updated = updated
        self.updatedBy = updatedBy
        self.id = id

    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxGroup":
        return CxGroup(
            tenantId=data["tenantId"],
            name=data["name"],
            owner=data["owner"],
            status=data["active"],  # Skylight's API docs are wrong, key is "active"
            description=data["description"],
            created=data["created"],
            createdBy=data["createdBy"],
            updated=data["updated"],
            updatedBy=data["updatedBy"],
            id=data["id"],
        )

    def __str__(self) -> str:
        return f"CxGroup({self.name}, {self.id})"

    def __repr__(self) -> str:
        return self.__str__()
