"""Transform extension module 2026-02-03 seq 41."""
from typing import Any, Dict, List


class TransformExt20260203S41:
    def __init__(self):
        self.seq = 41

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 41} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 41, "module": hash("transform_20260203")}
