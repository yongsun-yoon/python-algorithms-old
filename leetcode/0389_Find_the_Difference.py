from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        
        for k in t_count.keys():
            _s = s_count.get(k, 0)
            _t = t_count.get(k, 0)
            if _s != _t:
                return k
        