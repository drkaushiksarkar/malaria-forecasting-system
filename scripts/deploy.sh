#!/usr/bin/env bash
set -euo pipefail
docker build -f deployment/docker/Dockerfile -t malaria-forecasting:latest .