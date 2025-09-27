'''
Дан массив целых чисел nums. 
Найдите подмассив с наибольшей суммой и вернуть ее сумму.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

'''
#%%
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums)-1
        max_sum = sum(nums)
        print(f'{max_sum=}')
        while l <= r:
            sub_mass = nums[l:r+1]
            curr_sum = sum(sub_mass)
            print(f'{l=},{r=},{sub_mass=},{curr_sum=}')
            max_sum = max(curr_sum, max_sum)
            print(f'{nums[l]=} < {nums[r]=}')
            if nums[l] < nums[r]:
                l +=1
            else:
                r -= 1   
        
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res
    

s = Solution()
# res = s.maxSubArray([-2,1])
# assert res == 1

#nums = [1, 2,-1,-2,2,1,-2,1,4,-5,4]
nums = [-2,1,-3,4,-1,2,1,-5,4]
res = s.maxSubArray(nums)
res