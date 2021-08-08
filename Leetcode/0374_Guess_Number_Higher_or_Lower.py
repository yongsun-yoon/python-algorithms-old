class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        
        while l <= r:
            num = (l + r) // 2
            res = guess(num)
            
            if res == 0:
                return num
            elif res == -1:
                r = num - 1
            elif res == 1:
                l = num + 1
            print(num)
        
        return num
        