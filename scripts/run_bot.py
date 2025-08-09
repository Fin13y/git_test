"""Entry point for running the scalping bot."""
from memecoin_scalper.config import Config
from memecoin_scalper.trader import ScalpTrader


def main() -> None:
    config = Config()
    trader = ScalpTrader(config)
    trader.run_cycle()


if __name__ == "__main__":
    main()
