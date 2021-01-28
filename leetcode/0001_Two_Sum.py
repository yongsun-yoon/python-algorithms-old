from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in table:
                return [table[diff], i]
            else:
                table[num] = i
        

            