from enum import Enum

class PlatformStatus(Enum):
    pending: str
    accepted: str
    enabled: str
    disabled: str
    def __eq__(self, __o: object) -> bool: ...
