class Solution:
    def convert(self, s, idx):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels += [i.upper() for i in vowels]
        
        if s[0] in vowels:
            s += 'ma'
        else:
            s = s[1:] + s[0] + 'ma'
        s += 'a' * idx
        return s
            
        
    def toGoatLatin(self, S: str) -> str:
        S = S.split(' ')
        S = [self.convert(i, idx+1) for idx, i in enumerate(S)]
        S = ' '.join(S)
        return S