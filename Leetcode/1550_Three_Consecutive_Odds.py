from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        first, second = arr[0], arr[1]
        
        for third in arr[2:]:
            val = first * second * third
            if val % 2 != 0:
                return True
            first, second = second, third
            
        return False