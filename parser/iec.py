import re
from datetime import datetime
from typing import List

from smartobis.models import OBISCode, MeterValue, IECFrame
from smartobis.units.scaler import apply_scaler


LINE_RE = re.compile(
    r"(?P<obis>\d+\.\d+\.\d+)\((?P<val>[^*)]+)(\*(?P<unit>[^)]+))?\)"
)


class IECParser:

    @classmethod
    def parse(cls, raw: str, ip: str, port: int) -> IECFrame:

        lines = raw.splitlines()

        values: List[MeterValue] = []
        frame_time = None

        for line in lines:
            line = line.strip()

            # Timestamp
            if line.startswith("0.9.1"):
                time = cls._extract(line)

            elif line.startswith("0.9.2"):
                date = cls._extract(line)
                frame_time = cls._parse_datetime(date, time)

            # Regular OBIS
            else:
                m = LINE_RE.match(line)
                if not m:
                    continue

                obis = OBISCode.from_string(m["obis"])
                value = float(m["val"])
                unit = m["unit"]

                values.append(
                    MeterValue(
                        obis=obis,
                        value=value,
                        unit=unit,
                        timestamp=frame_time
                    )
                )

        return IECFrame(
            source_ip=ip,
            port=port,
            timestamp=frame_time,
            raw=raw,
            values=values
        )

    @staticmethod
    def _extract(line: str) -> str:
        return line.split("(")[1].split(")")[0]

    @staticmethod
    def _parse_datetime(d, t):

        # 260225 + 134500 → 2026-02-25 13:45:00
        return datetime.strptime(
            d + t, "%d%m%y%H%M%S"
        )
