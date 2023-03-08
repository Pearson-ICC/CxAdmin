from typing import Any

class CxBusinessHoursItem:
    def __init__(
        self,
        tenantId: str,
        createdBy: str,
        updated: str,
        name: str,
        timezone: str,
        active: bool,
        description: str,
        startTimeMinutes: dict[str, Any],
        endTimeMinutes: dict[str, Any],
        created: str,
        updatedBy: str,
        id: str,
        exceptions: list[str],
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> "CxBusinessHoursItem": ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
