class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total = 0
        balance = 0
        for _s in s:
            balance += 1 if _s == 'R' else -1
            if balance == 0:
                total += 1
        return total