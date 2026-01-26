"""Transform extension module 2026-01-26 seq 235."""
from typing import Any, Dict, List


class TransformExt20260126S235:
    def __init__(self):
        self.seq = 235

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 235} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 235, "module": hash("transform_20260126")}
