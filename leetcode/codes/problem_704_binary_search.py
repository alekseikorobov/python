#%%
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums,l,r,t):
            while l <= r:
                m = ((r - l)//2) + l
                print(f'{m=},{l=},{r=}')
                if nums[m] == t:
                    return m
                elif t < nums[m]:
                    r = m - 1
                    print(f'left {r=}')
                    return bin_search(nums,l,r,t)
                elif t > nums[m]:
                    l = m + 1
                    print(f'right {l=}')
                    return bin_search(nums,l,r,t)
            return -1
        return bin_search(nums,0,len(nums)-1,target)
    
    
s = Solution()
res = s.search([-1,0,3,5,9,12],13)
print(res)