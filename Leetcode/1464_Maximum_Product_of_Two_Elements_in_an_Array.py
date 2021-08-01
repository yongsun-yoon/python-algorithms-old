from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1, num2 = 0, 0
        for n in nums:
            if n > num1:
                num1, num2 = n, num1
            elif n > num2:
                num2 = n
        return (num1 - 1) * (num2 - 1)