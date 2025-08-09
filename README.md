# Memecoin Scalper

This repository contains boilerplate code and file structure for a Solana-based
memecoin scalping bot. The bot scans for trending, high-volume tokens and aims
to enter and exit positions for 20-30% profit targets automatically.

## Structure

- `src/memecoin_scalper/` – Core package containing configuration, strategy,
  and trading logic stubs.
- `scripts/` – Executable scripts, including `run_bot.py` to trigger a single
  trading cycle.
- `tests/` – Pytest-based tests verifying basic behaviour.
- `requirements.txt` – Python dependencies required for development.

## Running

```bash
pip install -r requirements.txt
python scripts/run_bot.py
```

This project is a starting point; real-world trading requires additional error
handling, risk management, and infrastructure components.

