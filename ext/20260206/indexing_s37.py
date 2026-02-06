"""Indexing extension module 2026-02-06 seq 37."""
from typing import Any, Dict, List


class IndexingExt20260206S37:
    def __init__(self):
        self.seq = 37

    def run(self, data: List[Dict[str, Any]]) -> List[Dict]:
        return [{**d, "ext": "indexing", "seq": 37} for d in data if d.get("id")]

    def stats(self) -> Dict[str, int]:
        return {"seq": 37, "module": hash("indexing_20260206")}
