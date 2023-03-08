from typing import Protocol


class CSVAble(Protocol):
    def toCSV(self, headers: bool = True) -> list[str]:
        ...
