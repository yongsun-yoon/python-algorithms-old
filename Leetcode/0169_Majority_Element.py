from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        
        for num in nums:
            if cnt == 0:
                vote = num
                cnt += 1
            else:
                if vote == num:
                    cnt += 1
                else:
                    cnt -= 1
        return vote
