"""Ingestion extension module 2026-01-05 seq 38."""
from typing import Any, Dict, List


class IngestionExt20260105S38:
    def __init__(self):
        self.seq = 38

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "ingestion", "seq": 38} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 38, "module": hash("ingestion_20260105")}
