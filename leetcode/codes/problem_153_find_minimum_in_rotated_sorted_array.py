from typing import List

class Solution:
    def bin_search_min(self,nums,l,r):
        #print(nums,l,r)
        if r - l == 1:
            return nums[l]
        else:
          m = l + (r-l)//2
          #print(nums[m],m)
          
          left_element = self.bin_search_min(nums,l, m)
          right_element = self.bin_search_min(nums,m, r)
          
          return min(left_element,right_element)
        
    def findMin(self, nums: List[int]) -> int:
        return self.bin_search_min(nums,0,len(nums))
      

s = Solution()
# print(s.findMin([1]))

# print(s.findMin([1,2]))

print(s.findMin([3, 1,2]))


# чужое решение
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]