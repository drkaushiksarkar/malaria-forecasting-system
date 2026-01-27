"""Ingestion extension module 2026-01-27 seq 4."""
from typing import Any, Dict, List


class IngestionExt20260127S4:
    def __init__(self):
        self.seq = 4

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "ingestion", "seq": 4} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 4, "module": hash("ingestion_20260127")}
