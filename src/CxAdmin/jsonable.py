from typing import Protocol, Any
import json_fix  # type: ignore


class JSONSerializable(Protocol):
    def to_json(self) -> dict[str, Any]:
        ...

    def __json__(self) -> dict[str, Any]:
        return self.to_json()
