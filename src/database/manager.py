import os
import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger

DATABASE_URL = os.getenv("DATABASE_URL")

def get_engine():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL not set")
    return create_engine(DATABASE_URL, pool_pre_ping=True)

def fetch_latest_data(table="malaria_cases"):
    eng = get_engine()
    q = text(f"SELECT * FROM {table} ORDER BY year, month;")
    df = pd.read_sql(q, eng)
    logger.info(f"Loaded {len(df)} rows from {table}")
    return df

def write_forecasts(df: pd.DataFrame, table="malaria_forecasts"):
    eng = get_engine()
    df.to_sql(table, eng, if_exists="append", index=False)
    logger.info(f"Wrote {len(df)} forecast rows to {table}")