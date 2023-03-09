from typing import Any
from enum import Enum
from CxAdmin.jsonable import JSONSerializable

class PlatformStatus(JSONSerializable, Enum):
    pending: str
    accepted: str
    enabled: str
    disabled: str
    def __eq__(self, __o: object) -> bool: ...
    def to_json(self) -> dict[str, Any]: ...
