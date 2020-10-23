import string

class Solution:
    def recursive(self, n, alphabet):
        if n == 0: return ''
        
        base = len(alphabet)
        s = n // base
        r = n % base
        if r == 0:
            s -= 1
            r = base        
        
        return self.recursive(s, alphabet) + alphabet[r-1]
    
    def convertToTitle(self, n: int) -> str:
        alphabet = list(string.ascii_uppercase)
        return self.recursive(n, alphabet)
        