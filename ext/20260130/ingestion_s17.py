"""Ingestion extension module 2026-01-30 seq 17."""
from typing import Any, Dict, List


class IngestionExt20260130S17:
    def __init__(self):
        self.seq = 17

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "ingestion", "seq": 17} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 17, "module": hash("ingestion_20260130")}
