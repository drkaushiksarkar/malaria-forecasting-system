"""Validation extension module 2026-02-17 seq 237."""
from typing import Any, Dict, List


class ValidationExt20260217S237:
    def __init__(self):
        self.seq = 237

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "validation", "seq": 237} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 237, "module": hash("validation_20260217")}
