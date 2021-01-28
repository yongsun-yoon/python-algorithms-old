from typing import List
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        place = {}
        for idx, num in enumerate(nums):
            place.setdefault(num, [])
            place[num].append(idx)
        
        degree, ans = 0, 1e5
        for k, v in place.items():
            sub_degree = len(v)
            sub_len = max(v) - min(v) + 1
            if (sub_degree > degree) or (sub_degree == degree and ans > sub_len):
                degree = len(v)
                ans = sub_len
        
        return ans