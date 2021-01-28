class Solution:
    
    def check(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 2 == 1:
            return False
        else:
            return self.check(n / 2)
        
    def isPowerOfTwo(self, n: int) -> bool:
        return self.check(n)
                