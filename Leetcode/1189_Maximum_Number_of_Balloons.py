from collections import Counter

class Solution:
    # # using Counter wise operations
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     cnt = Counter(text)
    #     balloon = Counter('balloon')
    #     ans = 0
        
    #     while True:
    #         if cnt & balloon == balloon:
    #             ans += 1
    #         else:
    #             break
    #         cnt -= balloon
        
    #     return ans

    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt = {i:cnt[i] for i in 'balloon'}
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values())