from enum import Enum


class PlatformStatus(Enum):
    pending = "pending"
    accepted = "accepted"
    enabled = "enabled"
    disabled = "disabled"

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, PlatformStatus):
            return self.value == __o.value
        return False
