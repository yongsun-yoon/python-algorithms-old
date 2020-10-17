class Solution:
    def addDigits(self, num: int) -> int:
        ## while loop method
        # while num >= 10:
        #     num = sum(map(int, str(num)))
        # return num
        
        ## remainder method
        ## 어떤 숫자를 9로 나눈 나머지는 그 숫자의 자리수를 더한 수를 9로 나눈 나머지와 같다.
        return 0 if num == 0 else (num - 1) % 9 + 1
        
