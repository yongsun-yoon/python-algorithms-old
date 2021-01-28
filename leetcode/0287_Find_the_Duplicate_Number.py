from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for n in nums:
            if n - prev == 0:
                return n
            else:
                prev = n
        