from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not k : return True
        
        curr_k = k
        for n in nums:
            if n == 0:
                curr_k += 1
            else:
                if curr_k < k:
                    return False
                else:
                    curr_k = 0
        return True