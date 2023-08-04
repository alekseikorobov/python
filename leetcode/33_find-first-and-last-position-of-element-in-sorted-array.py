from typing import List


class Solution:

    def search(self, nums: List[(int,int)], target:int):
        
        N = len(nums)

        lc = int(N/2)
        rc = N - lc
        
        if N == 1: 
            if nums[0][1] == target:return nums[0]
            else: return False
        else:
            lm = nums[0:lc]
            rc = nums[rc:]
            self.search(lm,target)



    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]

        if not target in nums: return res

        

        pass



s = Solution()

print(s.searchRange([5,7,7,8,8,10], target = 8), [3,4])
print(s.searchRange(nums = [], target = 0), [-1,-1])
