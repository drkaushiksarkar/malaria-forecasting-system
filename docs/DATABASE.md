# Database

## Engine
- SQLAlchemy + psycopg2
- URL via `DATABASE_URL` (e.g. `postgresql+psycopg2://user:pass@host:5432/malaria`)

## Tables
### `malaria_cases`
Stores monthly historicals + covariates.

| column               | type               | notes                           |
|----------------------|--------------------|----------------------------------|
| id (PK)              | serial             |                                  |
| upazilaid            | int                | entity id                        |
| year                 | int                | YYYY                             |
| month                | int                | 1..12                            |
| population           | int                |                                  |
| pv                   | int                | PV cases                         |
| pf                   | int                | PF cases                         |
| mixed                | int                | Mixed cases                      |
| average_temperature  | double precision   |                                  |
| total_rainfall       | double precision   |                                  |
| relative_humidity    | double precision   |                                  |
| average_ndvi         | double precision   |                                  |
| average_ndwi         | double precision   |                                  |
| UNIQUE (upazilaid, year, month) |         |                                  |

### `malaria_forecasts`
Stores forecast results by month.

| column        | type               | notes                         |
|---------------|--------------------|-------------------------------|
| id (PK)       | serial             |                               |
| upazilaid     | int                |                               |
| target        | varchar(32)        | pv_rate \| pf_rate \| mixed_rate |
| year          | int                | forecast month year           |
| month         | int                | forecast month                |
| mean          | double precision   | point forecast                |
| lower_90      | double precision   | 90% PI lower                  |
| upper_90      | double precision   | 90% PI upper                  |
| forecast_date | timestamptz        | default `now()`               |

Schemas live in `src/database/schema.sql`.

## Migrations
- Place SQL migrations in `src/database/migrations/`.
- (Optional) Adopt Alembic if you want versioned migrations.

## Common Ops
- Initialize:
  ```bash
  python scripts/setup_database.py
  ```
- Bulk load historicals:
  ```bash
  python scripts/load_historical_data.py /path/to/historicals.csv
  ```

## Permissions
- Minimum: INSERT/SELECT on `malaria_forecasts`, SELECT on `malaria_cases`.
