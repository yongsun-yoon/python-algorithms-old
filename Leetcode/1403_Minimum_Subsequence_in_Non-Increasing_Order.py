from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        remain_sum = sum(nums)
        
        current = []
        current_sum = 0
        while current_sum <= remain_sum:
            n = nums.pop()
            current.append(n)
            current_sum += n
            remain_sum -= n
        
        return current
