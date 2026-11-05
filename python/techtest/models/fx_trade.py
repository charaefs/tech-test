from __future__ import annotations

from datetime import datetime

from techtest.models.base_trade import BaseTrade


class FxTrade(BaseTrade):
    FX_SPOT_TRADE_TYPE = "FxSpot"
    FX_FORWARD_TRADE_TYPE = "FxFwd"

    def __init__(self, trade_id:str, trade_type:str) -> None:
        super().__init__(trade_id, trade_type)
        self.value_date: datetime = datetime.min
