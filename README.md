# Malaria Forecasting System

Streaming malaria forecasting as a service:
- Ingests data from PostgreSQL
- Generates forecasts (PV/PF/Mixed rates), verifies against observations, and can fine-tune
- Exposes a REST API (FastAPI)
- Schedulable batch runs
- Docker/Kubernetes ready
- CI/CD via GitHub Actions

## Key Features
- **Forecasting**: multi-step malaria rate forecasts per Upazila.
- **Verification**: SMAPE, RMSE, MAE, coverage@90% with JSONL logs.
- **Fine-tuning**: optional incremental updates when error/coverage degrades.
- **DB I/O**: SQLAlchemy reads/writes from/to PostgreSQL.
- **Ops**: Docker, docker-compose, K8s manifests, GHCR publish, tests, lint.

## Quickstart (Local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
# (optional) start postgres via compose
docker compose -f deployment/docker/docker-compose.yml up -d db
python scripts/setup_database.py
uvicorn src.service.main:app --port 8080 --reload
```
Open http://127.0.0.1:8000/docs

Trigger a forecast:
```bash
curl -X POST http://127.0.0.1:8000/forecast/run   -H 'content-type: application/json'   -d '{"target":"pv_rate","horizon":3}'
```

## Repository Map
See `docs/ARCHITECTURE.md` and `docs/DEPLOYMENT.md`.

## License & Notices
- License: MIT (see `LICENSE`)
- Notices: see `NOTICE` (if present)
- Developers: see `DEVELOPERS.md`
