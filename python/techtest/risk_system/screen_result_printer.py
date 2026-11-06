from __future__ import annotations

from techtest.models import ScalarResults


class ScreenResultPrinter:
    def print_results(self, results: ScalarResults) -> None:
        for result in results:
            # add_error accepts None, so a trade could in theory have neither a result nor an error
            if result.result is None and result.error is None: 
                print(result.trade_id)
            elif result.result is None:
                print(f"{result.trade_id} : {result.error}")
            elif result.error is None:
                print(f"{result.trade_id} : {result.result}")
            else:
                print(f"{result.trade_id} : {result.result} : {result.error}")