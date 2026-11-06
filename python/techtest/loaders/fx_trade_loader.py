from __future__ import annotations

from datetime import datetime

from techtest.models import FxTrade
from techtest.loaders.base_trade_loader import BaseTradeLoader


class FxTradeLoader(BaseTradeLoader):
    _SEPARATOR = "¬"
    _HEADER_LINES = 2

    def _create_trade_from_line(self, line: str) -> FxTrade:
        items = line.split(self._SEPARATOR)
        trade = FxTrade(items[8], items[0])
        trade.trade_date = datetime.fromisoformat(items[1])
        trade.instrument = items[2]+items[3]
        trade.notional = float(items[4])
        trade.rate = float(items[5])
        trade.value_date = datetime.fromisoformat(items[6])
        trade.counterparty = items[7]

        return trade

