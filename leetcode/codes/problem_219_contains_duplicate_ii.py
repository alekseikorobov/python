#%%
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #99,99 k=1
        #0,99,198
        
        ps = [0]*(len(nums)+1)
        for i in range(len(nums)):
            ps[i+1] = nums[i] + ps[i]
            
            
        print(f'{nums=},{k=}')
        print(f'{len(ps)},{ps=}')
        prev = 0
        for i in range(0,k):
            if i >= len(ps):
                print('break')
                break
            s_now = ps[i] - ps[1]
            print(s_now)
            if s_now == prev:
                return True
            prev = s_now
        print('second')
        for i in range(1,len(ps)):
            a = (k)+i
            print(f'{i=}, {a=}')
            if a >= len(ps):
                print('break')
                break
            
            s_now = ps[a] - ps[i]
            print(s_now)
            if s_now == prev:
                return True
            prev = s_now
        
        
        # for i in range(len(nums)):
        #     part = nums[i:i + k+1]
        #     l = len(part)
        #     if l < 2: continue
        #     print(part)
        #     if len(set(part))<l:
        #         return True
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(i - j) > k: continue
        #         condition = (nums[i] == nums[j])
        #         if condition:
        #             return True
        return False
    
s = Solution()
#s.containsNearbyDuplicate([1,0,1,1],1)
#s.containsNearbyDuplicate([1,2,3,1,2,3],2)
#s.containsNearbyDuplicate([1,2,3,1],3)
s.containsNearbyDuplicate([99,99],2)
#%%

#чужое решение, я не смог решить!
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        
        return False

