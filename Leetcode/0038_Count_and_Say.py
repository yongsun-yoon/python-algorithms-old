class Solution:
    def convert(self, num:str):
        converted, curr, cnt = '', '', 0
        for idx, n in enumerate(num):
            if n == curr:
                cnt += 1
            else:
                if idx > 0:
                    converted += f'{cnt}{curr}'
                curr = n
                cnt = 1
                
        converted += f'{cnt}{curr}' 
        return converted
        
        
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.convert(self.countAndSay(n-1))