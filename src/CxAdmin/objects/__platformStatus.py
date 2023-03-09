from enum import Enum
from CxAdmin.jsonable import JSONSerializable
from typing import Any


class PlatformStatus(JSONSerializable, Enum):
    pending = "pending"
    accepted = "accepted"
    enabled = "enabled"
    disabled = "disabled"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PlatformStatus):
            return self.value == __o.value
        return False

    def to_json(self) -> dict[str, Any]:
        return self.value
