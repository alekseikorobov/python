#%%
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        

        for a in range(len(nums)):
            f = nums[a]
            t = f - 1
            print(f'{a=},{t=}')
            end = -1
            for i in range(len(nums)-1,-1,-1):
                if nums[i] == f:
                    end = i
                if nums[i] == t:
                    if end == -1:
                        end = i                    
                    print(nums[a:end+1])
                    return len([x for x in nums[a:end+1] if x in [f,t]])
        return 0
        #b = len(nums)-1

        # b = len(nums)-1
        # # min_el = nums[a]
        # # max_el = nums[b]
        # max_size = 0
        # for a in range(len(nums)):
        #     for b in range(a+1,len(nums)):
        #     #while a>b:
        #         if nums[b] - nums[a] == 1:
        #             curr_size = len([x for x in nums[a:b] if x < nums[b]])
        #             if max_size < curr_size:
        #                 max_size  = curr_size
            
        # return max_size
s = Solution()
#s.findLHS([1,3,2,2,5,2,3,7]) #5
s.findLHS([1,2,3,4]) #2



#%%
# не смог решить, чужое решение:
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums.sort()

        l,r = 0, 1
        size = 0
        while r < len(nums):
            t = nums[r] - nums[l]
            if t == 1:
                size = max(size,r - l + 1)            
            if t <= 1:
                r+=1
            elif t > 1:
                l+=1
        return size