from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        cnt = [i for i,j in cnt.items() if i == j]
        return max(cnt) if cnt else -1