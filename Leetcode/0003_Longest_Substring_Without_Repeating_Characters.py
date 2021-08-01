class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        max_len = 0
        sub_s = ''
        
        for _s in s:
            if _s in sub_s:
                sub_s = sub_s[sub_s.index(_s)+1:]
            sub_s += _s
            max_len = max(len(sub_s), max_len)
            
        return max_len