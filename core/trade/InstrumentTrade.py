from dataclasses import dataclass


@dataclass
class InstrumentTrade:
    instrument_from: str
    instrument_to: str
    quantity: float = 0.0
