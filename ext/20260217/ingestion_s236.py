"""Ingestion extension module 2026-02-17 seq 236."""
from typing import Any, Dict, List


class IngestionExt20260217S236:
    def __init__(self):
        self.seq = 236

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "ingestion", "seq": 236} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 236, "module": hash("ingestion_20260217")}
