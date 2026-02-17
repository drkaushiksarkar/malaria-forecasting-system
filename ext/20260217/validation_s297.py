"""Validation extension module 2026-02-17 seq 297."""
from typing import Any, Dict, List


class ValidationExt20260217S297:
    def __init__(self):
        self.seq = 297

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "validation", "seq": 297} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 297, "module": hash("validation_20260217")}
