from __future__ import annotations

import importlib
import os
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from typing import Iterable

from techtest.models import PricingEngine, ResultReceiver, Trade
from techtest.risk_system.pricing_config_loader import PricingConfigLoader


class ParallelPricer:
    # Maximum number of trades being priced at the same time
    _MAX_WORKERS = 16

    def __init__(self) -> None:
        self._pricers: dict[str, PricingEngine] = {}

    def price(self, trade_containers: Iterable[Iterable[Trade]], result_receiver: ResultReceiver) -> None:
        self._load_pricers()

        with ThreadPoolExecutor(max_workers=self._MAX_WORKERS) as executor:
            in_flight = set()

            for trade_container in trade_containers:
                for trade in trade_container:
                    if trade.trade_type not in self._pricers:
                        result_receiver.add_error(trade.trade_id, "No Pricing Engines available for this trade type")
                        continue

                    if len(in_flight) >= self._MAX_WORKERS:
                        done, in_flight = wait(in_flight, return_when=FIRST_COMPLETED)
                        for future in done:
                            future.result()   # re-raises any error from the worker

                    pricer = self._pricers[trade.trade_type]
                    in_flight.add(executor.submit(pricer.price, trade, result_receiver))

            # Wait for the last ones before returning
            for future in wait(in_flight).done:
                future.result()

    def _load_pricers(self) -> None:
        pricing_config_loader = PricingConfigLoader()
        pricing_config_loader.config_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "pricing_config", "PricingEngines.xml")
        pricer_config = pricing_config_loader.load_config()

        for config_item in pricer_config:
            module = importlib.import_module(config_item.module)
            pricer_class = getattr(module, config_item.class_name)
            pricer = pricer_class()

            self._pricers[config_item.trade_type] = pricer
