from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, Iterator

from techtest.models import Trade


class BaseTradeLoader(ABC):
    # Reads a delimited trade feed file. Subclasses describe the file format and how to build each trade.

    # Set by subclasses
    _SEPARATOR: str
    _HEADER_LINES: int

    def __init__(self, data_file: str) -> None:
        self.data_file = data_file

    def load_trades(self) -> Iterable[Trade]:
        return self._load_trades_from_file(self.data_file)

    def _load_trades_from_file(self, filename: str) -> Iterator[Trade]:
        # utf-8-sig skips the byte order mark at the start of the file
        with open(filename, encoding="utf-8-sig") as stream:
            for _ in range(self._HEADER_LINES):
                next(stream, None)  # Skip the header lines

            for line in stream:
                if line.split(self._SEPARATOR)[0] == "END":
                    break
                yield self._create_trade_from_line(line.rstrip("\r\n"))

    @abstractmethod
    def _create_trade_from_line(self, line: str) -> Trade:
        ...