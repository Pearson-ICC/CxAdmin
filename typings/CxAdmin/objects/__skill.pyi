from datetime import datetime
from typing import Any
from CxAdmin.jsonable import JSONSerializable

class Skill(JSONSerializable):
    id: str
    name: str
    proficiency: int
    added: datetime
    def __init__(
        self, id: str, name: str, proficiency: int, added: datetime
    ) -> None: ...
    @staticmethod
    def from_json(data: dict[str, Any]) -> Skill: ...
    def to_json(self) -> dict[str, Any]: ...
