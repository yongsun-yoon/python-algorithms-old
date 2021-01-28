from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rlen, clen = len(image), len(image[0])
        orgColor = image[sr][sc]
        
        def dfs(r, c):
            if 0 <= r < rlen and 0 <= c < clen and image[r][c] == orgColor:
                image[r][c] = newColor
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

        if orgColor != newColor:
            dfs(sr, sc)
        return image