class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = [(idx, i, i.isalpha()) for idx, i in enumerate(s)]
        alphas = [i[1] for i in s if i[2]]
        non_alphas = [i for i in s if not i[2]]
        reversed_alphas = alphas[::-1]
        
        for i in non_alphas:
            reversed_alphas.insert(i[0], i[1])
        res = ''.join(reversed_alphas)
        return res
