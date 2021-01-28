class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows < 2:
            return s
        
        pos = [i for i in range(numRows)] + [i for i in range(numRows-2, 0, -1)]
        pos = {i:j for i,j in enumerate(pos)}
        result = [[] for _ in range(numRows)]
        
        for i in range(len(s)):
            idx = pos[i % (2 *numRows - 2)]
            result[idx].append(s[i])
        
        result = ''.join([''.join(i) for i in result])            
        return result