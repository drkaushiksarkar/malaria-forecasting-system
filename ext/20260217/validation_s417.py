"""Validation extension module 2026-02-17 seq 417."""
from typing import Any, Dict, List


class ValidationExt20260217S417:
    def __init__(self):
        self.seq = 417

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "validation", "seq": 417} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 417, "module": hash("validation_20260217")}
