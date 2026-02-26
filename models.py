from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class OBISCode:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int = 255

    @classmethod
    def from_string(cls, s: str):
        parts = s.split(".")
        parts += ["255"] * (6 - len(parts))
        return cls(*map(int, parts))

    def __str__(self):
        return f"{self.a}.{self.b}.{self.c}.{self.d}.{self.e}.{self.f}"


@dataclass
class MeterValue:
    obis: OBISCode
    value: float
    unit: Optional[str]
    timestamp: Optional[datetime]
    scaler: int = 0
    quality: Optional[str] = None


@dataclass
class IECFrame:
    source_ip: str
    port: int
    timestamp: datetime
    raw: str
    values: list[MeterValue]
