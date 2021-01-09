from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        r, c = len(board), len(board[0])
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    ans += 1
        
        return ans