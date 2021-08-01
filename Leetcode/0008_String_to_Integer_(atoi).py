class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        
        if s[0] in ['+', '-']:
            sign = 1 if s[0] == '+' else -1
            s = s[1:]
        else:
            sign = 1
        
        num = ''
        for _s in s:
            if _s.isdigit():
                num += _s
            else:
                break
        
        i = sign * int(num) if num.isdigit() else 0
        i = min(i, 2**31-1)
        i = max(i, -2**31)
        return i