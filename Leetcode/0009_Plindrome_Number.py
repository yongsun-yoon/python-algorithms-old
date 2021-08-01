class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        tmp, rev = x, 0
        while tmp:
            rev = rev * 10 + tmp % 10
            tmp = tmp // 10
        return x == rev
