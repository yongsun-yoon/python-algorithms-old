from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        aliquot = []
        for i in range(1, int(area**0.5)+1):
            if area % i == 0:
                aliquot.append([area//i, i])
        
        return aliquot[-1]
        