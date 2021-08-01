from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start, dest = map(set, zip(*paths))
        ans = list(dest - start)[0]
        return ans