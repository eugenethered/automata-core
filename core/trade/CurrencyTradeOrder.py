from dataclasses import dataclass


@dataclass
class CurrencyTradeOrder:
    currency_from: str
    currency_to: str
    quantity: int
    side: str
