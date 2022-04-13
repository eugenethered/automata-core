from dataclasses import dataclass, field
from enum import Enum


class Status(Enum):
    NEW = 'new'
    SUBMITTED = 'submitted'
    CANCELLED = 'cancelled'
    EXECUTED = 'executed'
    ERROR = 'error'


@dataclass
class InstrumentTrade:
    instrument_from: str
    instrument_to: str
    quantity: float
    status: Status = field(default=Status.NEW)
    description: str = field(default=None)
