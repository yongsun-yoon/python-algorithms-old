from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:        
        cnt = {}
        for n in nums:
            cnt.setdefault(n, 0)
            cnt[n] += 1
        
        ans = 0
        for v in cnt.values():
            ans += (v * (v-1)) / 2
        return int(ans)