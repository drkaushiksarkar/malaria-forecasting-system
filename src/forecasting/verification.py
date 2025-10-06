import os, json
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error

def smape(y, p): return 100 * np.mean(2*np.abs(p - y) / (np.abs(y) + np.abs(p) + 1e-8))

class VerificationEngine:
    def __init__(self, verification_path):
        self.verification_path = verification_path
        os.makedirs(verification_path, exist_ok=True)
        self.log_file = os.path.join(verification_path, "verification_log.jsonl")

    def verify_forecasts(self, forecast, actual_df, target_col):
        upa = forecast["upazila_id"]
        act = actual_df[actual_df["UpazilaID"] == upa]
        pts, errs = [], []
        for i, month in enumerate(forecast["months"]):
            row = act[(act["year"] == month["year"]) & (act["month"] == month["month"])]
            if not row.empty and row.iloc[0][target_col] is not None:
                a = float(row.iloc[0][target_col])
                f = float(forecast["mean"][i])
                lb = float(forecast["lower_90"][i])
                ub = float(forecast["upper_90"][i])
                e = abs(a - f)
                pts.append({"year": month["year"], "month": month["month"], "actual": a,
                            "forecast": f, "lower_90": lb, "upper_90": ub,
                            "error": e, "in_interval": lb <= a <= ub})
                errs.append(e)
        if pts:
            actuals = np.array([p["actual"] for p in pts])
            preds = np.array([p["forecast"] for p in pts])
            metrics = {
                "upazila_id": upa,
                "target": target_col,
                "verification_date": datetime.utcnow().isoformat(),
                "n_verified": len(pts),
                "mae": float(np.mean(errs)),
                "rmse": float(np.sqrt(mean_squared_error(actuals, preds))),
                "smape": float(smape(actuals, preds)),
                "coverage_90": float(np.mean([p["in_interval"] for p in pts])),
                "verified_points": pts
            }
        else:
            metrics = {
                "upazila_id": upa, "target": target_col,
                "verification_date": datetime.utcnow().isoformat(),
                "n_verified": 0, "message": "No matching observations."
            }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(metrics) + "\n")
        return metrics