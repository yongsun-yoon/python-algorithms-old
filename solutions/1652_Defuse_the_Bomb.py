from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        len_code = len(code)
        
        for i in range(len_code):
            if k == 0:
                ans.append(0)
            elif k > 0:
                ans.append(sum([code[(i + _k) % len_code] for _k in range(1, k+1)]))
            else:
                ans.append(sum([code[(i + _k) % len_code] for _k in range(k, 0)]))
    
        return ans