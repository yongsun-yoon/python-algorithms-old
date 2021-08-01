from collections import Counter
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        A = [Counter(a) for a in A]
        
        common = A[0]
        for a in A[1:]:
            common &= a
        
        return common.elements()