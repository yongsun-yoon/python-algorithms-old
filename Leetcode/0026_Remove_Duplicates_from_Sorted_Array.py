from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        now, idx = -1e7, 0        
        
        while idx < len(nums):
            if now < nums[idx]:
                now = nums[idx]
                idx += 1
            else:
                nums.pop(idx)
            
        return len(nums)