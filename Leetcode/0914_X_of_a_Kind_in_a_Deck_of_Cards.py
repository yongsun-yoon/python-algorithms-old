import math
from collections import Counter
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck).values()
        cnt = list(cnt)
        gcd = cnt[0]
        
        for c in cnt[1:]:
            gcd = math.gcd(gcd, c)
        
        return gcd > 1