class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum([_s=='1' for _s in s])

        zeros = 1 if s[0] == '0' else 0
        ones -= 0 if s[0] == '0' else 1
        score = zeros + ones
        
        for _s in s[1:-1]:
            if _s == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros + ones, score)
        
        return score