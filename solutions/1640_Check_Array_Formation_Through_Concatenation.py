from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_map = {p[0]:p for p in pieces}
        result = []
        
        for n in arr:
            result += piece_map.get(n, [])
        
        return arr == result