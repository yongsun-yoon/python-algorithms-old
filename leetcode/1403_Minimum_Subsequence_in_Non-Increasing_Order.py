from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        total_sum = sum(nums)
        
        res = []
        while sum(res) <= sum(nums):
            n = nums.pop()
            res.append(n)
        
        return res
