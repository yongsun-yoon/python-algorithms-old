from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        idx = len(A) - 1
        
        while idx > 0:
            s, r = divmod(A[idx], 10)
            A[idx] = r
            A[idx-1] += s
            idx -= 1
        
        while A[0] > 9:
            s, r = divmod(A[0], 10)
            A[0] = r
            A.insert(0, s)
            
        return A