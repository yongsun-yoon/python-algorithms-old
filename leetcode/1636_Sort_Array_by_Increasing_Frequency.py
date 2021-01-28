from typing import List
import collections

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        ans = sorted(nums, key=lambda x : [freq[x], -x])
        return ans