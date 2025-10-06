import os, time
from datetime import datetime
from croniter import croniter
import requests

CRON = os.getenv("CRON_EXPRESSION", "*/30 * * * *")
SERVICE_URL = os.getenv("SERVICE_URL", "http://localhost:8080/forecast/run")

def main():
    base = datetime.now()
    itr = croniter(CRON, base)
    next_run = itr.get_next(datetime)
    while True:
        now = datetime.now()
        if now >= next_run:
            try:
                requests.post(SERVICE_URL, json={"target":"pv_rate","horizon":6}, timeout=60)
                print(f"[{now}] Triggered batch")
            except Exception as e:
                print(f"Scheduler error: {e}")
            next_run = itr.get_next(datetime)
        time.sleep(5)

if __name__ == "__main__":
    main()