from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
from ..database import fetch_latest_data, write_forecasts
from ..forecasting import ForecastEngine, VerificationEngine, FineTuningEngine
from ..data.preprocessing import preprocess_streaming_data

router = APIRouter(prefix="/forecast", tags=["Forecasting"])

class ForecastRequest(BaseModel):
    target: str = "pv_rate"
    horizon: int = 6

@router.post("/run")
def run_forecast(req: ForecastRequest):
    df = fetch_latest_data("malaria_cases")
    # Minimal preprocess (derive target column if present)
    indicators = ["average_temperature","total_rainfall","relative_humidity","average_ndvi","average_ndwi"]
    dfp = preprocess_streaming_data(df, [c.title().replace("_","") for c in []], req.target) if False else df  # using db-ready cols

    # Stub engines (plug in real models/artifacts)
    fe = ForecastEngine(None, None, None, None, None, {
        "SEQ_LEN": 12,
        "INDICATORS": ["Average_temperature","Total_rainfall","Relative_humidity","Average_NDVI","Average_NDWI"],
    })

    out_rows = []
    for upa in sorted(df["upazilaid"].unique()):
        fc = fe.forecast(df.rename(columns=str.title), upa, req.target, req.horizon)
        for (m, y), mean, lb, ub in zip(
            [(d["month"], d["year"]) for d in fc["months"]], fc["mean"], fc["lower_90"], fc["upper_90"]
        ):
            out_rows.append({"upazilaid": upa, "target": req.target, "year": y, "month": m,
                             "mean": mean, "lower_90": lb, "upper_90": ub, "forecast_date": fc["forecast_date"]})
    out_df = pd.DataFrame(out_rows)
    write_forecasts(out_df, "malaria_forecasts")
    return {"status": "ok", "inserted": len(out_df)}