class Solution:
    # def convert_base_2(self, num):
    #     if num < 2:
    #         return str(num)
    #     else:
    #         s, r = divmod(num, 2)
    #         return self.convert_base_2(s) + str(r)
    
    # def bitwiseComplement(self, N: int) -> int:
    #     base_2 = self.convert_base_2(N)
    #     complement = ''.join(['0' if i == '1' else '1' for i in base_2])
    #     ans = int(complement, 2)
    #     return ans

    def bitwiseComplement(self, N: int) -> int:
        P = 2
        while P <= N:
            P *= 2
        return P - 1 - N