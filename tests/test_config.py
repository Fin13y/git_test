from memecoin_scalper.config import Config


def test_default_profit_target() -> None:
    cfg = Config()
    assert 0 < cfg.profit_target < 1
