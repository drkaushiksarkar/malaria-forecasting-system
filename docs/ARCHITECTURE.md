# Architecture

## Overview
The system ingests monthly malaria data, generates multi-step forecasts by Upazila, verifies predictions against newly observed data, and (optionally) triggers fine-tuning based on error/coverage thresholds.

## Components
- **API (FastAPI)** — `/forecast/run` endpoint to trigger a batch forecast.
- **Database Layer (SQLAlchemy)** — adapters for reading `malaria_cases` and writing to `malaria_forecasts`.
- **Forecasting**
  - `ForecastEngine` — multi-step forecasting per entity.
  - `VerificationEngine` — computes MAE/RMSE/SMAPE/Coverage@90, logs JSONL.
  - `FineTuningEngine` — policy for deciding and performing incremental training (stub hooks).
- **Scheduler** — optional cron-based HTTP trigger for periodic runs.
- **Ops** — Docker, Compose, K8s, GHCR image publish, CI.

## Data Flow
1. **Read** latest observations & features from `malaria_cases`.
2. **Preprocess** (feature engineering, target rates if provided).
3. **Forecast** next `horizon` months per Upazila.
4. **Write** `mean`, `lower_90`, `upper_90` into `malaria_forecasts`.
5. **Verify** past forecasts when matching actuals arrive.
6. **Fine-tune** if thresholds are exceeded.

## Configuration
- YAML: `config/config.yaml`
- Env: `.env`
- Logging: `config/logging.yaml`

## Extending
- Replace stub models with your VAE/GAN code in `src/models` and integrate in `src/forecasting/engine.py`.
- Introduce artifact loading (scalers/encoders) and move hard-coded columns to config.
- Add new endpoints (e.g., retrieval APIs).
