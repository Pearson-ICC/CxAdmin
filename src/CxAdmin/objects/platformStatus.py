from enum import Enum


class PlatformStatus(Enum):
    pending = "pending"
    accepted = "accepted"
    enabled = "enabled"
    disabled = "disabled"
