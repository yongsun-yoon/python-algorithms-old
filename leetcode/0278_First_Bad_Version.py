# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    return True

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            curr = (l + r) // 2
            if isBadVersion(curr):
                r = curr
            else:
                l = curr + 1
                
        return l