from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            cnt = sum([i >= x for i in nums])
            if x == cnt:
                return x
        return -1
        