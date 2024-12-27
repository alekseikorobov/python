from typing import List


class Solution:

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        N = len(nums)

        sum_res = float('inf')
        min_diff = abs(sum_res - target)

        for index1 in range(N):

            index2 = index1 + 1
            index3 = N - 2            
            while index2 < index3:
                sum_part = nums[index1] + nums[index2] + nums[index3]
                if sum_part == target:
                    yield index1, index2, index3
                
                min_diff_new = abs(sum_part - target)
                if min_diff_new < min_diff:
                    min_diff = min_diff_new
                    sum_res = sum_part
                    yield index1, index2, index3
                elif sum_part > target:
                    index3 -= 1
                    yield None,None,None
                else:
                    index2 += 1
        

    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        N = len(nums)

        for index1 in range(N):

            index2 = index1 + 1
            index3 = N - 2
            index4 = N - 1
            
            for i1,i2,i3 in self.threeSum(nums,target):
                print(f'{i1=},{i2=},{i3=}')


s = Solution()

print(s.fourSum([1,0,-1,0,-2,2],0) )