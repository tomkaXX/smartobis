from typing import List
from smartobis.models import MeterValue


class LoadProfile:

    def __init__(self):
        self.entries: List[list[MeterValue]] = []

    def add_block(self, values):
        self.entries.append(values)

    def completeness(self):

        if not self.entries:
            return 0.0

        filled = sum(len(e) for e in self.entries)
        expected = len(self.entries) * len(self.entries[0])

        return filled / expected
