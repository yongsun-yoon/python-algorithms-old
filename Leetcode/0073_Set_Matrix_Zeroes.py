from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_row = set()
        zero_col = set()
        
        for _m in range(m):
            for _n in range(n):
                if matrix[_m][_n] == 0:
                    zero_row.add(_m)
                    zero_col.add(_n)
        
        for r in zero_row:
            for _n in range(n):
                matrix[r][_n] = 0
        
        for c in zero_col:
            for _m in range(m):
                matrix[_m][c] = 0

        