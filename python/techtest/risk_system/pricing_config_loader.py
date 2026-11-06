from __future__ import annotations

import xml.etree.ElementTree as ET

from techtest.risk_system.pricing_engine_config import PricingEngineConfig
from techtest.risk_system.pricing_engine_config_item import PricingEngineConfigItem


class PricingConfigLoader:
    def __init__(self) -> None:
        self.config_file: str | None = None

    def load_config(self) -> PricingEngineConfig:
        if self.config_file is None or not self.config_file.strip():
            raise ValueError("A valid non null, non empty config_file path must be provided")
        
        config_list = PricingEngineConfig()

        tree = ET.parse(self.config_file)
        root = tree.getroot()

        for engine in root.findall("Engine"):
            item = PricingEngineConfigItem(
                trade_type=engine.get("tradeType"), 
                module=engine.get("module"), 
                class_name=engine.get("class"))

            config_list.append(item)

        return config_list

