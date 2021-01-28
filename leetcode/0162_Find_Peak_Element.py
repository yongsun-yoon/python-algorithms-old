from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        prev = nums[0]
        prev_diff = 0
        
        for idx, n in enumerate(nums[1:]):
            diff = n - prev
            
            if 0 < prev_diff and diff < 0:
                return idx
            else:
                prev = n
                prev_diff = diff
        
        return nums.index(max(nums))