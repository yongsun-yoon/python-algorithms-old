from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for idx, i in enumerate(nums):
            if (i in table) and (idx - table[i] <= k):
                return True
            else:
                table[i] = idx
        return False
        