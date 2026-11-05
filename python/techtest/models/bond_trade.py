from __future__ import annotations

from techtest.models.base_trade import BaseTrade


class BondTrade(BaseTrade):
    GOV_BOND_TRADE_TYPE = "GovBond"
    CORP_BOND_TRADE_TYPE = "CorpBond"

    def __init__(self, trade_id: str, trade_type: str) -> None:
        super().__init__(trade_id, trade_type)
