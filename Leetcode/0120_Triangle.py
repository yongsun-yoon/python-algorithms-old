from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle) - 1
        for i in range(depth)[::-1]:
            width = len(triangle[i])
            for j in range(width):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]