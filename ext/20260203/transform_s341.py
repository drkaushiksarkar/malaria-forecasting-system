"""Transform extension module 2026-02-03 seq 341."""
from typing import Any, Dict, List


class TransformExt20260203S341:
    def __init__(self):
        self.seq = 341

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 341} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 341, "module": hash("transform_20260203")}
