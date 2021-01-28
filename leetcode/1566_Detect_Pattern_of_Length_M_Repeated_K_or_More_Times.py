from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        pattern_len = m*k
        for i in range(0, len(arr)-(pattern_len)+1):
            piece = arr[i:i+m]
            pred = piece * k
            true = arr[i:i+pattern_len]
            if pred == true:
                return True
        
        return False