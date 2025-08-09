"""Main trading engine for the scalping bot."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .config import Config
from .execution import Order, SolanaClient
from .strategies import MarketData, should_enter, should_exit
from .trending import fetch_trending_tokens


@dataclass
class Position:
    token: str
    amount: float
    entry_price: float


class ScalpTrader:
    """High-level orchestration of the scalping strategy."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self.client = SolanaClient(config.rpc_endpoint)
        self.positions: List[Position] = []

    def run_cycle(self) -> None:
        """Execute a single trading cycle."""
        for symbol in fetch_trending_tokens():
            market_data = self._get_market_data(symbol)
            if should_enter(market_data, self.config.profit_target):
                self._enter_position(symbol, market_data.price)

        for position in list(self.positions):
            current_price = self._get_market_price(position.token)
            if should_exit(position.entry_price, current_price, self.config.profit_target):
                self._exit_position(position, current_price)

    # --- Internal helpers -------------------------------------------------
    def _get_market_data(self, symbol: str) -> MarketData:
        # Placeholder for fetching price/volume data
        return MarketData(price=1.0, volume_24h=2_000_000)

    def _get_market_price(self, symbol: str) -> float:
        # Placeholder for getting the current market price
        return 1.25

    def _enter_position(self, symbol: str, price: float) -> None:
        order = Order(token=symbol, amount=1.0, side="buy")
        self.client.submit_order(order)
        self.positions.append(Position(token=symbol, amount=1.0, entry_price=price))

    def _exit_position(self, position: Position, price: float) -> None:
        order = Order(token=position.token, amount=position.amount, side="sell")
        self.client.submit_order(order)
        self.positions.remove(position)
