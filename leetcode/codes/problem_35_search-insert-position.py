from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        for i in range(0,N):
            if nums[i] == target:
                return i            
            if nums[i] > target:
                return i
        return N



s = Solution()

print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))
print(s.searchInsert([1,3,5,6],0))
print(s.searchInsert([3,6,7,8,10],5))
