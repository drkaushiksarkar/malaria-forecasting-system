# Deployment

## Environment
Copy and edit `.env.example` -> `.env`.

Important variables:
- `DATABASE_URL` — Postgres connection string
- `APP_PORT` — default 8080
- `MODEL_ROOT`, `STREAM_DATA_PATH`, `VERIFICATION_PATH` — model & data paths
- `CRON_EXPRESSION` — if using the scheduler

## Docker (local)
```bash
docker build -f deployment/docker/Dockerfile -t malaria-forecasting:latest .
docker run --env-file .env -p 8080:8080 malaria-forecasting:latest
```

## docker-compose (API + Postgres)
```bash
docker compose -f deployment/docker/docker-compose.yml up -d
# initialize DB
python scripts/setup_database.py
```

## Kubernetes (example)
1. Push an image to GHCR (use the `docker-publish.yml` workflow via a tag).
2. Update image in `deployment/kubernetes/deployment.yaml`:
   ```
   ghcr.io/OWNER/malaria-forecasting-system:TAG
   ```
3. Apply:
   ```bash
   kubectl apply -f deployment/kubernetes/configmap.yaml
   kubectl apply -f deployment/kubernetes/deployment.yaml
   kubectl apply -f deployment/kubernetes/service.yaml
   ```

## CI (GitHub Actions)
- `ci.yml` — lint (ruff/black) + pytest
- `docker-publish.yml` — publish Docker on semver tag `v*.*.*` to GHCR

## Releases
- Create a tag `vX.Y.Z` and push — Action builds/pushes docker image.

## Scaling & Observability
- Scale replica count in K8s `Deployment`.
- Add log sinks / metrics:
  - log level & file via `config/logging.yaml`
  - Prometheus (add FastAPI instrumentation if needed)

## Security Notes
- Use read-only DB user for the API if possible.
- Consider enabling request auth (Basic/OAuth) at FastAPI layer if exposed publicly.
- Require signed commits & protected branches for the repo.
