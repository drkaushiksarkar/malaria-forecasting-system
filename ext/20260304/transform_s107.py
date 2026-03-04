"""Transform extension module 2026-03-04 seq 107."""
from typing import Any, Dict, List


class TransformExt20260304S107:
    def __init__(self):
        self.seq = 107

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 107} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 107, "module": hash("transform_20260304")}
