import itertools

class Solution:
    # def maxPower(self, s: str) -> int:
    #     curr_str, curr_power, max_power = '', 0, 0
        
    #     for _s in s:
    #         if _s == curr_str:
    #             curr_power += 1
    #         else:
    #             max_power = max(max_power, curr_power)
    #             curr_str = _s
    #             curr_power = 1
        
    #     max_power = max(max_power, curr_power)
    #     return max_power

    # using groupby
    def maxPower(self, s: str) -> int:
        ans = max([len(list(i)) for s, i in itertools.groupby(s)])
        return ans