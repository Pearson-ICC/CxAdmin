from datetime import datetime
from typing import Any


class Skill:
    id: str
    name: str
    proficiency: int
    added: datetime

    def __init__(
        self,
        id: str,
        name: str,
        proficiency: int,
        added: datetime,
    ):
        self.id = id
        self.name = name
        self.proficiency = proficiency
        self.added = added

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Skill":
        return Skill(
            id=data["id"],
            name=data["name"],
            proficiency=data["proficiency"],
            added=datetime.fromisoformat(data["added"][:-1]),
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "proficiency": self.proficiency,
            "added": self.added.isoformat(),
        }
