# malaria-forecasting-system

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Agents](https://img.shields.io/badge/Agentic_AI-FF6F00?style=flat-square)

Production malaria incidence forecasting with autonomous pipeline orchestration, Terraform-managed cloud infrastructure, and self-healing deployment.

---

## Architecture

```
                    AutonomousPipelineAgent
                    (self-healing orchestrator)
                            |
        +-------------------+-------------------+
        |                   |                   |
    Ingest              Validate             Train
    (HMIS, DHIS2,       (schema, range,      (gradient boosted
     climate API)        continuity)          ensemble, 24 features)
        |                   |                   |
        +-------------------+-------------------+
                            |
        +-------------------+-------------------+
        |                   |                   |
    Forecast            Verify              Deploy
    (multi-country,     (SMAPE, RMSE,       (Terraform, Docker,
     6-month horizon)    coverage@90)        health check)
                            |
                       AlertAgent
                    (anomaly detection,
                     severity classification,
                     rate-limited notifications)
```

## Agent system

The `agents/` package implements autonomous pipeline orchestration:

- **AutonomousPipelineAgent** -- Self-healing pipeline that orchestrates end-to-end forecasting: data ingestion, validation, model training, forecast generation, verification, and deployment. Detects failures, retries with exponential backoff, and falls back to last known good model.

- **AlertAgent** -- Monitors forecast outputs for anomalies using threshold-based and statistical detection. Classifies alert severity (info, warning, critical) and dispatches notifications with rate limiting to prevent alert storms.

## Components

| Module | Purpose |
|:-------|:--------|
| `agents/pipeline_agent.py` | Autonomous pipeline orchestration with checkpoint/resume |
| `agents/__init__.py` | Agent package exports |
| `forecasting/` | Model training, prediction, and verification |
| `ingestion/` | Data ingestion from HMIS, DHIS2, and climate APIs |
| `infrastructure/` | Terraform modules for AWS deployment |
| `api/` | FastAPI serving layer for forecast endpoints |

## Deployment

```bash
# Infrastructure provisioning
cd infrastructure && terraform init && terraform apply

# Docker deployment
docker build -t malaria-forecast .
docker run -p 8000:8000 malaria-forecast

# Run autonomous pipeline
python -m agents.pipeline_agent
```

## Monitoring

| Metric | Threshold | Alert |
|:-------|:----------|:------|
| SMAPE | < 0.15 | Warning if exceeded |
| RMSE | < 0.10 | Warning if exceeded |
| Coverage@90 | > 0.85 | Critical if below |
| Forecast deviation | > 50% baseline | Critical |

## License

MIT
