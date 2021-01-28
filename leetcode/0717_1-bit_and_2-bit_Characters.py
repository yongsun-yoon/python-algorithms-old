from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        wait = False
        for b in bits[:-1]:
            if wait:
                wait = False
            elif b == 1:
                wait = True
                
        return not wait
        