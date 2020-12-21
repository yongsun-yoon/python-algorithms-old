from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        idx, cnt = 1, 0
        
        while idx < len(flowerbed)-1:
            l, c, r = flowerbed[idx-1], flowerbed[idx], flowerbed[idx+1]
            if c or l or r:
                pass
            else:
                flowerbed[idx] = 1
                cnt += 1
            idx += 1

        return n <= cnt
                
            