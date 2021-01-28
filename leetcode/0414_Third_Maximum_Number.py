from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        val = [float('-inf')] * 3
        
        for n in nums:
            if n in val:
                pass
            elif n > val[0]:
                val[0], val[1], val[2] = n, val[0], val[1]
            elif n > val[1]:
                val[1], val[2] = n, val[1]
            elif n > val[2]:
                val[2] = n
        
        return max(val) if float('-inf') in val else val[2]
        
