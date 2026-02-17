"""Transform extension module 2026-02-17 seq 304."""
from typing import Any, Dict, List


class TransformExt20260217S304:
    def __init__(self):
        self.seq = 304

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "transform", "seq": 304} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 304, "module": hash("transform_20260217")}
