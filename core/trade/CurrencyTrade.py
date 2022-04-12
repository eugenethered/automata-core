from dataclasses import dataclass


@dataclass
class CurrencyTrade:
    currency_from: str
    currency_to: str
    quantity: int
    side: str
