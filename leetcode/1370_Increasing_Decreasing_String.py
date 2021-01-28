class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        ans = ''
        
        while s:
            small = sorted(set(s))
            for _s in small:
                ans += _s
                s.remove(_s)
            
            large = sorted(set(s), reverse=True)
            for _s in large:
                ans += _s
                s.remove(_s)
        return ans