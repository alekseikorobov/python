
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(0,l,2):
            if i + 1 >= l or (nums[i] != nums[i + 1]):
                return nums[i] 

#O(Nlogn) 