from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        mid = (len(mat) - 1) / 2
        
        for idx, row in enumerate(mat):
            ans += row[idx]
            if idx != mid:
                ans += row[-idx-1]
        
        return ans
        