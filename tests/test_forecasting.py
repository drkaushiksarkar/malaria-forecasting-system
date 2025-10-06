import pandas as pd
from src.forecasting.engine import ForecastEngine

def test_forecast_shape():
    fe = ForecastEngine(None,None,None,None,None,{"SEQ_LEN":1,"INDICATORS":[]})
    df = pd.DataFrame({"UpazilaID":[1], "year":[2024], "month":[12]})
    fc = fe.forecast(df, 1, "pv_rate", 3)
    assert len(fc["months"]) == 3