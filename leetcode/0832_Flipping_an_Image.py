from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in A:
            ans.append([1-i for i in row[::-1]])
        return ans