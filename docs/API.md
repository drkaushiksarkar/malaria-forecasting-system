# API

Base URL: `/`

OpenAPI docs:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Health
### GET `/`
Returns service status.

**200**
```json
{ "ok": true, "service": "malaria-forecasting" }
```

## Forecasts
### POST `/forecast/run`
Triggers a batch forecast over all available Upazilas using the latest data in PostgreSQL.

**Request**
```json
{
  "target": "pv_rate",     // one of: pv_rate | pf_rate | mixed_rate
  "horizon": 6             // months ahead (int > 0)
}
```

**Response**
```json
{
  "status": "ok",
  "inserted": 18   // number of forecast rows written to DB
}
```

**Behavior**
1. Loads data from `malaria_cases`.
2. (Optionally) preprocesses features/targets.
3. Runs multi-step forecast per Upazila.
4. Writes results to `malaria_forecasts`.

**Notes**
- Forecast numbers are 0.0 in the shipped stub; plug your models into `src/forecasting/engine.py`.
- Verification happens via `VerificationEngine` (see `src/forecasting/verification.py`).

### Errors
- `400` invalid payload
- `500` DB/service errors

## Future Endpoints (suggested)
- `GET /forecast/{upazilaid}?target=pv_rate` — retrieve forecasts
- `POST /forecast/verify` — run verification against latest actuals
- `POST /fine-tune` — trigger fine-tuning
