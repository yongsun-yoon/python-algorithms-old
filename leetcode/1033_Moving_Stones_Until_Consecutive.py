from typing import List

class Solution:    
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        ans = [-1, -1]
        
        if c - a == 2:
            ans[0] = 0
        elif c - b < 3 or b - a < 3:
            ans[0] = 1
        else:
            ans[0] = 2
        ans[1] = c - a -2 if ans[0] else 0
        
        return ans