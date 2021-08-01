class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: return "0"
        ans = ""
        
        while n > 0:
            n, r = divmod(n, 1000)
            r = '.' + str(r).zfill(3) if n != 0 else str(r)
            ans = r + ans
        return ans