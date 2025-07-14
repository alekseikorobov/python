from typing import List

class Solution:

    def get_first_index_pos(self, nums):
        l,r = 0,len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= 0:
                if m - 1 >= 0:
                    if nums[m-1] < 0:
                        return m
                    else:
                        r = m
                else:
                    return m
            elif nums[m] < 0:
                l = m + 1
        return -1
                

    def maximumCount(self, nums: List[int]) -> int:
        pos_index = self.get_first_index_pos(nums)
        print('pos_index',pos_index)
        start_index = pos_index
        while pos_index >= 0 and pos_index < len(nums) and nums[pos_index] == 0:
            pos_index += 1
        
        if start_index == -1:
            return len(nums)
        left_m = nums[0:start_index]
        print(left_m,start_index)
        left_count = len(left_m)
        right_count = len(nums[pos_index:])
        return max(left_count,right_count)

      

s = Solution()
print(s.get_first_index_pos([-2,-1,-1,1,2,3]))
print(s.get_first_index_pos([-2,-1,-1]))
print(s.get_first_index_pos([1,2,3]))

print(s.get_first_index_pos([x*-1 for x in range(6,0,-1)] + list(range(0,10))))
