class Solution:
    def reverse(self, x: int) -> int:
        sign = [-1, 1][x > 0]
        x = ''.join(reversed(str(abs(x))))
        x = sign * int(x)
        
        if abs(x) > 2 ** 31:
            x = 0
        return x