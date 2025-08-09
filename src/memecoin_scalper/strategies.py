"""Trading strategy logic."""
from dataclasses import dataclass


@dataclass
class MarketData:
    price: float
    volume_24h: float


def should_enter(data: MarketData, profit_target: float) -> bool:
    """Determine whether to enter a position."""
    # Placeholder logic: enter if volume is high; real logic would be more complex
    return data.volume_24h > 1_000_000


def should_exit(entry_price: float, current_price: float, profit_target: float) -> bool:
    """Determine whether to exit a position."""
    return current_price >= entry_price * (1 + profit_target)
