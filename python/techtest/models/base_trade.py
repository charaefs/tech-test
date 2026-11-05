from __future__ import annotations
from datetime import datetime

from techtest.models.trade import Trade


class BaseTrade(Trade):
    def __init__(self, trade_id: str, trade_type: str) -> None:

        if trade_id is None or not trade_id.strip():
            raise ValueError("A valid non null, non empty trade ID must be provided")
        if trade_type is None or not trade_type.strip():
            raise ValueError("A valid non null, non empty trade type must be provided")
        
        self.trade_date: datetime = datetime.min
        self.counterparty: str | None = None
        self.instrument: str | None = None
        self.notional: float = 0.0
        self.rate: float = 0.0
        
        self._trade_id = trade_id
        self._trade_type = trade_type

    @property
    def trade_type(self) -> str:
        return self._trade_type

    @property
    def trade_id(self) -> str:
        return self._trade_id
