"""Configuration settings for the scalping bot."""
from dataclasses import dataclass


@dataclass
class Config:
    """Runtime configuration for the trader.

    Attributes:
        rpc_endpoint: URL for the Solana RPC node.
        wallet_secret: Path to the wallet's secret key file.
        profit_target: Target profit percentage per trade (0.20 -> 20%).
        max_slippage: Maximum allowed slippage during order execution.
    """

    rpc_endpoint: str = "https://api.mainnet-beta.solana.com"
    wallet_secret: str = "~/.config/solana/id.json"
    profit_target: float = 0.25  # 25% profit target
    max_slippage: float = 0.01   # 1% slippage
