class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        i, j = 0, len(s)-1
        
        while i < j:
            isvowel_i = s[i] in vowels
            isvowel_j = s[j] in vowels
            
            if isvowel_i and isvowel_j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                i += 1 - isvowel_i
                j -= 1 - isvowel_j

        return ''.join(s)