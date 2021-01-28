from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged = sorted(merged)
        length = len(merged)
        index = length // 2
        
        if length % 2 == 0:
            median = (merged[index-1] + merged[index]) / 2
        else:
            median = merged[index]
        
        return median