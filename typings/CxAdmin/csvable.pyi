from typing import Protocol

class CSVAble(Protocol):
    def toCSV(self, headers: bool) -> list[str]: ...
