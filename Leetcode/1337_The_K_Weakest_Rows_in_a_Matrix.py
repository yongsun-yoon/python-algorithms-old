from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakness = [(sum(row), idx) for idx, row in enumerate(mat)]
        weakness = sorted(weakness, key=lambda x: (x[0], x[1]))
        return [i[1] for i in weakness[:k]]
