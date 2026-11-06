from __future__ import annotations

from datetime import datetime

from techtest.models import BondTrade
from techtest.loaders.base_trade_loader import BaseTradeLoader


class BondTradeLoader(BaseTradeLoader):
    _SEPARATOR = ","
    _HEADER_LINES = 1

    def _create_trade_from_line(self, line: str) -> BondTrade:
        items = line.split(self._SEPARATOR)
        trade = BondTrade(items[6], items[0])
        trade.trade_date = datetime.fromisoformat(items[1])
        trade.instrument = items[2]
        trade.counterparty = items[3]
        trade.notional = float(items[4])
        trade.rate = float(items[5])

        return trade
