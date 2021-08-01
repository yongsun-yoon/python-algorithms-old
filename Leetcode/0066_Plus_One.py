from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += add
            add = digits[i] // 10
            digits[i] %= 10
        
        if add == 1:
            digits.insert(0, 1)
        return digits