CREATE TABLE IF NOT EXISTS malaria_cases (
  id SERIAL PRIMARY KEY,
  upazilaid INTEGER NOT NULL,
  year INTEGER NOT NULL,
  month INTEGER NOT NULL,
  population INTEGER,
  pv INTEGER,
  pf INTEGER,
  mixed INTEGER,
  average_temperature DOUBLE PRECISION,
  total_rainfall DOUBLE PRECISION,
  relative_humidity DOUBLE PRECISION,
  average_ndvi DOUBLE PRECISION,
  average_ndwi DOUBLE PRECISION,
  UNIQUE (upazilaid, year, month)
);

CREATE TABLE IF NOT EXISTS malaria_forecasts (
  id SERIAL PRIMARY KEY,
  upazilaid INTEGER NOT NULL,
  target VARCHAR(32) NOT NULL,
  year INTEGER NOT NULL,
  month INTEGER NOT NULL,
  mean DOUBLE PRECISION,
  lower_90 DOUBLE PRECISION,
  upper_90 DOUBLE PRECISION,
  forecast_date TIMESTAMP WITH TIME ZONE DEFAULT now()
);