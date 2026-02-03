"""Transform extension module 2026-02-03 seq 251."""
from typing import Any, Dict, List


class TransformExt20260203S251:
    def __init__(self):
        self.seq = 251

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 251} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 251, "module": hash("transform_20260203")}
