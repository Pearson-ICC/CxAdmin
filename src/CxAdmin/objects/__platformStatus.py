from enum import Enum
import json_fix  # type: ignore


class PlatformStatus(Enum):
    pending = "pending"
    accepted = "accepted"
    enabled = "enabled"
    disabled = "disabled"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PlatformStatus):
            return self.value == __o.value
        return False

    def __json__(self) -> str:
        return self.value
