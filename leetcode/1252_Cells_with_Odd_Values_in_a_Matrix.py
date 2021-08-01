from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                res += (rows[i] + cols[j]) % 2
        
        return res