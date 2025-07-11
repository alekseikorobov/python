from typing import List


class Solution:
    
    def search(self, nums: List[int], target: int,l,r) -> List[int]:
        while l < r:
            m = ((r - l) //2) + l
            if nums[m] > target:
                r = m
                return self.search(nums,target,l,r)
            elif nums[m] < target:
                l = m + 1
                return self.search(nums,target,l,r)
            else:
                return True, m
        return False,-1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        is_exists, index = self.search(nums, target,0,len(nums))
        if is_exists:
            start_index = index
            end_index = index
            while start_index-1 >= 0 and nums[start_index-1] == target:
                start_index -= 1
            while end_index+1 < len(nums) and nums[end_index+1] == target:
                end_index += 1
            res = [start_index, end_index]
            return res
        
        return [-1,-1]
