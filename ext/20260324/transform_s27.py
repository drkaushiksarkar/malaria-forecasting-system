"""Transform extension module 2026-03-24 seq 27."""
from typing import Any, Dict, List


class TransformExt20260324S27:
    def __init__(self):
        self.seq = 27

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 27} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 27, "module": hash("transform_20260324")}
