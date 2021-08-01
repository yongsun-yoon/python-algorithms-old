from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        now = 0
        
        for n in nums:
            now += n
            ans.append(now)
        
        return ans