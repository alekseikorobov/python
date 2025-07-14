
# НЕ СМОГ РЕШИТЬ!
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        def get_permutation(nums, k):
            if k == 0: return []
            
            N = len(nums)
            
            result = []
            
            f,l = 1,0
            
            i = 0
            local_result = []
            start_add = False
            while f <= N and l < N:
                print('ff',f,'ll',l)
                if k == len(local_result):
                    result.append(local_result)
                    local_result = []
                    i = 0
                    if f == N:
                        l += 1
                        f = l
                   
                    #start_add = False
                    print('reset')
                else:
                    if l != f and f < N:
                        #if not start_add:
                        print('l',l,nums[l])
                        local_result.append(nums[l])
                        #start_add = True
                            
                        #if l != f:
                        print('f',f,nums[f])
                        local_result.append(nums[f])
                        print(f'{local_result=}')
                        #i += 1
                    else:
                        print('skip',l,f)
                    f += 1
            #result.append(local_result)
            return result
                
                
        
        result = []
        for k in [3]: #range(0,len(nums))
            r = get_permutation(nums, k)
            result.append(r)
        
        return result
    
    
s = Solution()

print(s.subsets([1,2,3,4]))

#ЧУЖОЕ РЕШЕНИЕ!!!
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def create(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            create(i+1)

            subset.pop()
            create(i+1)
        
        create(0)
        return res