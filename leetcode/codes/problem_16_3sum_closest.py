

from typing import List


class Solution:
    def __init__(self) -> None:
        pass

    def diff(x1,x2,x3, target):
        a = abs(target - abs(x1 + x2 + x3))
        return a    


    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: 
            a = abs(target - abs(nums[0] + nums[1]))
            b = abs(target - abs(nums[0]))
            c = abs(target - abs(nums[1]))
            
            if a < b and a < c:
                return nums[0] + nums[1]
            elif b < a and b < c:
                return nums[0]
            else:
                return nums[1]
            

        return 2