class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        ans = []
        
        dump = ''
        for s in S[::-1]:
            s = s.upper()
            dump = s + dump
            if len(dump) == K:
                ans.append(dump)
                dump = ''
        
        if len(dump) > 0:
            ans.append(dump)
        ans = '-'.join(ans[::-1])        
        return ans