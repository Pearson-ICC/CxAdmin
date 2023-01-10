from typing import Any

class CxQueue:
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
        active: str,
        activeVersion: str,
        id: str,
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxQueue": ...
    def __str__(self) -> str: ...
