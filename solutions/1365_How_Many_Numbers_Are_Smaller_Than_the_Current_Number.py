from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rank = sorted(nums)
        ans = [rank.index(n) for n in nums]
        return ans