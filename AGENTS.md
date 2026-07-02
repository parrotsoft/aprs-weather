# aprs-weather

Minimal APRS weather beacon script. Sends one position packet to APRS-IS and exits.

## Setup

- **Package manager**: `uv` (see `uv.lock` and `.venv/`)
- **Python**: 3.12 (`.python-version`)
- **Dependencies**: `aprslib>=0.7.2`, `python-dotenv>=1.2.2` (`pyproject.toml`)
- **Install**: `uv sync`
- **Environment**: Copy `.env.example` → `.env`, fill in `CALLSIGN`, `PASSCODE`, `LATITUDE`, `LONGITUDE`

## Run

```bash
uv run main.py
```

## Project structure

- `main.py` — single-file entrypoint. Reads env vars, connects to `rotate.aprs2.net:14580`, sends `CALLSIGN>APRS:=LAT/LON>comment`, and exits. Comment is hardcoded (`"Barranquilla 31°C"`).

## What's missing (add if needed)

No tests, no linting/formatting config, no CI, no pre-commit hooks, no CLI argument parsing, no daemon mode, no scheduling. Any of these must be set up from scratch.
