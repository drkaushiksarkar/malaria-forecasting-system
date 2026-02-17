"""Transform extension module 2026-02-17 seq 274."""
from typing import Any, Dict, List


class TransformExt20260217S274:
    def __init__(self):
        self.seq = 274

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 274} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 274, "module": hash("transform_20260217")}
