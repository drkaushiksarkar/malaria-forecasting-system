import pandas as pd, sys
from src.database.manager import get_engine
from sqlalchemy import text

def main(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("malaria_cases", get_engine(), if_exists="append", index=False)
    print(f"Loaded {len(df)} rows")
if __name__ == "__main__":
    main(sys.argv[1])