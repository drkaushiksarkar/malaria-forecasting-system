import os, pathlib
from sqlalchemy import text
from src.database.manager import get_engine

def main():
    sql_path = pathlib.Path("src/database/schema.sql")
    sql = sql_path.read_text()
    eng = get_engine()
    with eng.begin() as conn:
        for stmt in sql.split(";"):
            s = stmt.strip()
            if s:
                conn.execute(text(s))
    print("Database initialized.")
if __name__ == "__main__":
    main()