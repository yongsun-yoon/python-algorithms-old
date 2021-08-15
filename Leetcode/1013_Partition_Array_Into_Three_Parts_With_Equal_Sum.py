from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        avg, remain = divmod(sum(arr), 3)
        if remain: return False
        
        curr, cnt = 0, 0
        for i in arr:
            curr += i
            if curr == avg:
                cnt += 1
                curr = 0
        
        # if avg and curr % avg: return False
        return cnt >= 3