from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for idx, n in enumerate(nums):
            if total_sum == 2*left_sum + n:
                return idx
            else:
                left_sum += n
        
        return -1