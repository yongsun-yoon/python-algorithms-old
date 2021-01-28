from typing import List

class Solution:
    def dist(self, r, c, r0, c0):
        return abs(r-r0) + abs(c - c0)
    
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        nodes = [[i,j] for i in range(R) for j in range(C)]
        nodes = sorted(nodes, key=lambda x: self.dist(x[0], x[1], r0, c0))
        return nodes