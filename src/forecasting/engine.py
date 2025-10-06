import os, json
from datetime import datetime
import numpy as np
from ..data.features import build_feature_cols

class ForecastEngine:
    def __init__(self, vae, generator, feat_scaler, y_scalers, label_encoder, config):
        self.vae = vae
        self.generator = generator
        self.feat_scaler = feat_scaler
        self.y_scalers = y_scalers
        self.label_encoder = label_encoder
        self.config = config

    def forecast(self, df_context, upazila_id, target_col, horizon=6):
        df_upa = df_context[df_context["UpazilaID"] == upazila_id].sort_values(["year","month"])
        if len(df_upa) < self.config["SEQ_LEN"]:
            raise ValueError(f"Need at least {self.config['SEQ_LEN']} months")

        context = df_upa.iloc[-self.config["SEQ_LEN"]:]
        X = context[build_feature_cols(self.config["INDICATORS"])].values.astype(np.float32)
        if self.feat_scaler: X = self.feat_scaler.transform(X)

        # Placeholder: produce zeros
        months = []
        last = context.iloc[-1]
        for step in range(1, horizon+1):
            m = int((last["month"] - 1 + step) % 12 + 1)
            y = int(last["year"] + (last["month"] - 1 + step) // 12)
            months.append({"year": y, "month": m})

        return {
            "upazila_id": int(upazila_id),
            "target": target_col,
            "forecast_date": datetime.utcnow().isoformat(),
            "horizon": horizon,
            "months": months,
            "mean": [0.0]*horizon,
            "lower_90": [0.0]*horizon,
            "upper_90": [0.0]*horizon,
        }

    def save_forecast(self, forecast_dict, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(forecast_dict, f, indent=2)