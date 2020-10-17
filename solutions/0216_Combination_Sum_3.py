import itertools
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ## all combinations
        # ans = list(itertools.combinations(range(1, 10), k))
        # ans = [i for i in ans if sum(i) == n]
        # return ans
        
        ## backtracking
        ans = []
        self.backtrack(range(1, 10), k, n, [], ans)
        return ans
    
    def backtrack(self, nums, k, n, now, ans):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ans.append(now)
        
        for i in range(len(nums)):
            self.backtrack(nums[i+1:], k-1, n-nums[i], now + [nums[i]], ans)
            