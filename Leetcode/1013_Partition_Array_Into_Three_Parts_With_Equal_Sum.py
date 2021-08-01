from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        avg, rmd = divmod(sum(A), 3)
        part, cnt = 0, 0
        
        for a in A:
            part += a
            if part == avg:
                part = 0
                cnt += 1

        return (not rmd) and (cnt >= 3)