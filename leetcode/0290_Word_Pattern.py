class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        p2w, w2p = {}, {}
        
        if len(pattern) != len(s):
            return False
        
        for p, w in zip(pattern, s):
            pw = p2w.setdefault(p, w)
            wp = w2p.setdefault(w, p)
            
            if pw != w or wp != p:
                return False
        
        return True
