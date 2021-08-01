from typing import List

class Solution:
    def search(self, rr, rc, dr, dc, board):
        while 0 <= rr+dr <= 7 and 0 <= rc+dc <= 7:
            rr += dr
            rc += dc
            
            if board[rr][rc] == 'p':
                return 1
            elif board[rr][rc] == 'B':
                return 0
        return 0
    
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rr, rc = i, j
        
        return self.search(rr, rc, 1, 0, board) + self.search(rr, rc, -1, 0, board) + self.search(rr, rc, 0, 1, board) + self.search(rr, rc, 0, -1, board)
