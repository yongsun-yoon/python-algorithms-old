from collections import Counter

class Solution:
    def sum_digit(self, num):
        return sum(map(int, str(num)))
    
    def countLargestGroup(self, n: int) -> int:
        sums = [self.sum_digit(i) for i in range(1, n+1)]
        cnt =  Counter(sums)
        max_cnt = max(cnt.values())
        return len([i for i,j in cnt.items() if j == max_cnt])