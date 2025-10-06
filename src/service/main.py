import os, yaml
from fastapi import FastAPI
from loguru import logger
from .api import router as forecast_router

def load_logging():
    cfg = os.path.join("config", "logging.yaml")
    if os.path.exists(cfg):
        with open(cfg) as f:
            cfg = yaml.safe_load(f)
        logger.remove()
        logger.add(cfg["handlers"]["file"]["filename"], rotation="10 MB", level=cfg["level"])

app = FastAPI(title="Malaria Forecasting Service", version="0.1.0")
app.include_router(forecast_router)

@app.get("/")
def root(): return {"ok": True, "service": "malaria-forecasting"}

load_logging()