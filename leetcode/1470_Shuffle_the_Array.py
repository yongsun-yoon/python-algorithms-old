from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n == 1: return nums
            
        num1 = nums[:n]
        num2 = nums[n:]
        ans = []
        for i,j in zip(num1, num2):
            ans += [i, j]
        return ans