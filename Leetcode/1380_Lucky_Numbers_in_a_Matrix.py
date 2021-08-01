from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = {min(i) for i in matrix}
        col_max = {max(i) for i in zip(*matrix)}        
        return list(row_min & col_max)
                