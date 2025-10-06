import pandas as pd
from src.data.preprocessing import preprocess_streaming_data

def test_preprocess_ok():
    df = pd.DataFrame({
        "UpazilaID":[1,1],
        "year":[2024,2024],
        "month":[1,2],
        "Population":[100,100],
        "PV":[5,7],
        "Average_temperature":[25,26],
        "Total_rainfall":[10,20],
        "Relative_humidity":[70,72],
        "Average_NDVI":[0.3,0.31],
        "Average_NDWI":[0.1,0.2],
    })
    out = preprocess_streaming_data(df,
        ["Average_temperature","Total_rainfall","Relative_humidity","Average_NDVI","Average_NDWI"],
        "pv_rate")
    assert "pv_rate" in out.columns
